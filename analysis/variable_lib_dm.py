from databuilder.ehrql import Dataset
from databuilder.tables.beta.tpp import (
    clinical_events,
)

# Diabetes mellitus variable library
# Business Rules for Quality and Outcomes Framework (QOF) 2021/22 (Version 46)
# Clinical data extraction criteria
from variable_lib_helper import (
    last_matching_event,
    age_as_of,
    died_as_of,
    practice_registration_as_of,
)

import codelists


class DatasetFactory():
    def __init__(self, index_date) -> Dataset:
        self.index_date = index_date
        self.dataset = Dataset()
        # Define clinical events prior to index_date
        self.prior_events = clinical_events.take(clinical_events.date.is_on_or_before(index_date))
        # Define variable indicating whether a patient has died
        # Note: Although this is not in the business rules I'm including this as an
        # additional check
        self.has_not_died = ~died_as_of(index_date)

        # GMS reg status: Select patients who meet either of the criteria below:
        # Registered for GMS prior to or on the achievement date and did not
        # subsequently deregister from GMS (currently registered for GMS).
        # Registered for GMS prior to or on the achievement date and subsequently
        # deregistered from GMS after the achievement date (previously registered for
        # GMS). (i.e. patients who were registered for GMS on the achievement date).
        # TODO Note that this currently does not follow the qualifying criteria in the
        # business rules.
        practice_reg = practice_registration_as_of(index_date)
        self.gms_registration_status = practice_reg.exists_for_patient()

    def add_diabetes_mellitus_register_variables(self):
        # Field number 4
        # PAT_AGE: The age of the patient in full years at the achievement date.
        self.dataset.pat_age = age_as_of(self.index_date)
        # Field number 6
        # DMLAT_DAT: Date of the most recent diabetes diagnosis up to and including the
        # achievement date.
        self.dataset.dm_lat_dat = last_matching_event(self.prior_events, codelists.dm_cod).date
        # Field number 7
        # DMRES_DAT: Date of the most recent diabetes diagnosis resolved code recorded
        # after the most recent diabetes diagnosis and up to and including the
        # achievement date.
        self.dataset.dm_res_dat = last_matching_event(self.prior_events, codelists.dm_res_cod).date

from databuilder.ehrql import Dataset
from databuilder.tables.beta.tpp import (
    clinical_events,
    patients,
    practice_registrations,
)

# Diabetes mellitus variable library
# Business Rules for Quality and Outcomes Framework (QOF) 2021/22 (Version 46)
# Clinical data extraction criteria
from variable_lib_helper import (
    first_matching_event,
    last_matching_event,
    age_as_of,
    died_as_of,
    practice_registration_as_of,
)

import codelists


# Create dataset
dataset = Dataset()


# Define clinical events prior to index_date
def get_prior_events(index_date):
    return clinical_events.take(clinical_events.date.is_on_or_before(index_date))


# Define variable indicating whether a patient has died
# Note: Although this is not in the business rules I'm including this as an
# additional check
def get_has_not_died(index_date):
    return ~died_as_of(index_date)


# GMS reg status: Select patients who meet either of the criteria below:
# Registered for GMS prior to or on the achievement date and did not
# subsequently deregister from GMS (currently registered for GMS).
# Registered for GMS prior to or on the achievement date and subsequently
# deregistered from GMS after the achievement date (previously registered for
# GMS). (i.e. patients who were registered for GMS on the achievement date).
# TODO Note that this currently does not follow the qualifying criteria in the
# business rules.
def get_gms_registration_status(index_date):
    practice_reg = practice_registration_as_of(index_date)
    return practice_reg.exists_for_patient()


# Define all variables needed for the diabetes mellitus (dm) register (reg)
def add_diabetes_mellitus_register_variables(dataset, index_date):
    prior_events = get_prior_events(index_date)
    # Field number 4
    # PAT_AGE: The age of the patient in full years at the achievement date.
    dataset.pat_age = age_as_of(index_date)
    # Field number 6
    # DMLAT_DAT: Date of the most recent diabetes diagnosis up to and
    # including the achievement date.
    dataset.dm_lat_dat = last_matching_event(prior_events, codelists.dm_cod).date
    # Field number 7
    # DMRES_DAT: Date of the most recent diabetes diagnosis resolved code
    # recorded after the most recent diabetes diagnosis and up to and
    # including the achievement date.
    dataset.dm_res_dat = last_matching_event(prior_events, codelists.dm_res_cod).date
    return dataset

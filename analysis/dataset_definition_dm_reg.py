from datetime import date, timedelta

from databuilder.ehrql import Dataset, case, when
from databuilder.tables.beta.tpp import (
    clinical_events,
    patients,
    practice_registrations,
)

import codelists
from variable_lib_helper import (
    first_matching_event,
    last_matching_event,
    age_as_of,
    died_as_of,
    practice_registration_as_of,
)

# Payment Period End Date (PPED)
index_date = date(2022, 3, 31)

# Create dataset
dataset = Dataset()

# Define clinical events prior to index_date
prior_events = clinical_events.take(clinical_events.date.is_on_or_before(index_date))

# Define variable indicating whether a patient has died
# Note: Although this is not in the business rules I'm including this as an
# additional check
has_not_died = ~died_as_of(index_date)


# GMS reg status: Select patients who meet either of the criteria below:
# Registered for GMS prior to or on the achievement date and did not
# subsequently deregister from GMS (currently registered for GMS).
# Registered for GMS prior to or on the achievement date and subsequently
# deregistered from GMS after the achievement date (previously registered for
# GMS). (i.e. patients who were registered for GMS on the achievement date).
# TODO Note that this currently does not follow the qualifying criteria in the
# business rules.
practice_reg = practice_registration_as_of(index_date)
gms_registration_status = practice_reg.exists_for_patient()

# Define clinical data extraction criteria

# Field number 4
# PAT_AGE: The age of the patient in full years at the achievement date.
dataset.pat_age = age_as_of(index_date)

# Field number 6
# DMLAT_DAT: Date of the most recent diabetes diagnosis up to and including the
# achievement date.
dataset.dm_lat_dat = last_matching_event(prior_events, codelists.dm_cod).date

# Field number 7
# DMRES_DAT: Date of the most recent diabetes diagnosis resolved code recorded
# after the most recent diabetes diagnosis and up to and including the
# achievement date.
dataset.dm_res_dat = last_matching_event(prior_events, codelists.dm_res_cod).date

########################################################
# Define Business Rules for Diabetes register (RM_REG) #
########################################################

# DM_REG: Rule number 1:
# Pass to the next rule all patients from the specified population who meet
# both of the criteria below:  Have a diabetes diagnosis in the patient record
# up to and including the achievement date. Latest diabetes diagnosis is not
# followed by a diabetes resolved code.
dm_reg_r1 = (dataset.dm_res_dat < dataset.dm_lat_dat) | (
    dataset.dm_lat_dat.is_not_null() & dataset.dm_res_dat.is_null()
)

# DM_REG: Rule number 2:
# Reject patients passed to this rule who are aged under 17 years old on the
# achievement date.
dm_reg_r2 = ~(dataset.pat_age < 17)

# Apply business rules to set population
dataset.set_population(
    gms_registration_status
    & dm_reg_r1
    & dm_reg_r2
    & has_not_died
    )

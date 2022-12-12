from datetime import date, timedelta

from variable_lib_dm import (
    DatasetFactory
)

# Define index date
# Use Payment Period End Date (PPED) for NHS FY2021/22
index_date = date(2022, 3, 31)
factory = DatasetFactory(index_date)
factory.add_diabetes_mellitus_register_variables()
dataset = factory.dataset
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
dataset.set_population(factory.gms_registration_status & dm_reg_r1 & dm_reg_r2 & factory.has_not_died)

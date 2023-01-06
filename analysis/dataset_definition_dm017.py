from datetime import date, timedelta

from variable_lib_dm import (
    get_has_not_died,
    dataset,
    get_gms_registration_status,
    add_diabetes_mellitus_register_variables,
    get_dm_reg_r1,
    get_dm_reg_r2,
)

# Define index date
# Use Payment Period End Date (PPED) for NHS FY2021/22
index_date = date(2022, 3, 31)

# Define variables for study population
has_not_died = get_has_not_died(index_date)
gms_registration_status = get_gms_registration_status(index_date)

# Create dataset and add diabetes register variables
dataset = add_diabetes_mellitus_register_variables(dataset, index_date)

########################################################
# Define Business Rules for Diabetes register (RM_REG) #
########################################################

# DM_REG rule 1:
dataset.dm_reg_r1 = get_dm_reg_r1()

# DM_REG rule 2:
dataset.dm_reg_r2 = get_dm_reg_r2()

dm_reg_select_r2 = dataset.dm_reg_r1 & ~dataset.dm_reg_r2

# Apply business rules to set population
dataset.set_population(
    # GMS registration status
    gms_registration_status
    & has_not_died
    # Business rules for DM_REG
    & dm_reg_select_r2
)

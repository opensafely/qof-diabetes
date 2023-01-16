from datetime import date, timedelta

from variable_lib_dm import (
    DmDataset,
    get_has_not_died,
    get_gms_registration_status,
)

# Define index date
# Use Payment Period End Date (PPED) for NHS FY2021/22
index_date = date(2022, 3, 31)

# Define variables for study population
has_not_died = get_has_not_died(index_date)
gms_registration_status = get_gms_registration_status(index_date)

# Create dataset and add diabetes mellitus variables
dataset = DmDataset()
dataset.add_diabetes_mellitus_variables(index_date)

# DM_REG rule 1:
dataset.dm_reg_r1 = dataset.get_dm_reg_r1()

# DM_REG rule 2:
dataset.dm_reg_r2 = dataset.get_dm_reg_r2()

# DM020 rule 1:
dataset.dm020_r1 = dataset.get_dm020_dm021_r1()

# DM020 rule 2:
dataset.dm020_r2 = dataset.get_dm020_dm021_r2(58.0, index_date)

# DM020 rule 3:
dataset.dm020_r3 = dataset.get_dm020_dm021_r3(index_date)

# DM020 rule 4:
dataset.dm020_r4 = dataset.get_dm020_dm021_r4(index_date)

# DM020 rule 5:
dataset.dm020_r5 = dataset.get_dm020_dm021_r5(index_date)

# DM020 rule 6:
dataset.dm020_r6 = dataset.get_dm020_dm021_r6(index_date)

# DM020 rule 7:
dataset.dm020_r7 = dataset.get_dm020_dm021_r7(index_date)

# DM020 rule 8:
dataset.dm020_r8 = dataset.get_dm020_dm021_r8(58.0, index_date)

# DM020 rule 9:
dataset.dm020_r9 = dataset.get_dm020_dm021_r9(index_date)

# DM020 rule 10:
dataset.dm020_r10 = dataset.get_dm020_dm021_r10(index_date)

# Define select action for DM_REG
dm_reg_select_r2 = dataset.dm_reg_r1 & ~dataset.dm_reg_r2

# Define first select action for DM020 (Rule 2)
dm020_select_r2 = ~dataset.dm020_r1 & dataset.dm020_r2

# Define second select action for DM020 (Rule 10)
dm020_select_r10 = (
    ~dataset.dm020_r1
    & ~dataset.dm020_r2
    & ~dataset.dm020_r3
    & ~dataset.dm020_r4
    & ~dataset.dm020_r5
    & ~dataset.dm020_r6
    & ~dataset.dm020_r7
    & ~dataset.dm020_r8
    & ~dataset.dm020_r9
    & ~dataset.dm020_r10
)

# Apply business rules to set population
dataset.set_population(
    # GMS registration status
    has_not_died
    & gms_registration_status
    # Business rules for DM_REG
    & dm_reg_select_r2
    # Business rules for DM020
    & (dm020_select_r2 | dm020_select_r10)
)

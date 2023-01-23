from datetime import date

from dm_dataset import DmDataset

# Define index date
# Use Payment Period End Date (PPED) for NHS FY2021/22
# Create dataset and add diabetes mellitus variables
dataset = DmDataset(index_date=date(2022, 3, 31), ifcchba_cutoff_val=58.0)
dataset.add_diabetes_mellitus_variables()

# DM_REG rule 1:
dataset.dm_reg_r1 = dataset.get_dm_reg_r1()

# DM_REG rule 2:
dataset.dm_reg_r2 = dataset.get_dm_reg_r2()

# DM020 rule 1:
dataset.dm020_r1 = dataset.get_dm020_r1()

# DM020 rule 2:
dataset.dm020_r2 = dataset.get_dm020_r2()

# DM020 rule 3:
dataset.dm020_r3 = dataset.get_dm020_r3()

# DM020 rule 4:
dataset.dm020_r4 = dataset.get_dm020_r4()

# DM020 rule 5:
dataset.dm020_r5 = dataset.get_dm020_r5()

# DM020 rule 6:
dataset.dm020_r6 = dataset.get_dm020_r6()

# DM020 rule 7:
dataset.dm020_r7 = dataset.get_dm020_r7()

# DM020 rule 8:
dataset.dm020_r8 = dataset.get_dm020_r8()

# DM020 rule 9:
dataset.dm020_r9 = dataset.get_dm020_r9()

# DM020 rule 10:
dataset.dm020_r10 = dataset.get_dm020_r10()

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
    # Business rules for DM_REG
    dm_reg_select_r2
    # Business rules for DM020
    & (dm020_select_r2 | dm020_select_r10)
)

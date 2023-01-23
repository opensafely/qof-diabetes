from datetime import date

from dm_dataset import DmDataset

# Define index date as `date(2022, 3, 31)`
# Use Payment Period End Date (PPED) for NHS FY2021/22
# Create dataset and add diabetes mellitus variables
dataset = DmDataset(index_date=date(2022, 3, 31))
dataset.add_diabetes_mellitus_variables()

# Diabetes register (DM_REG) rule 1:
dataset.dm_reg_r1 = dataset.get_dm_reg_r1()

# Diabetes register (DM_REG) rule 2:
dataset.dm_reg_r2 = dataset.get_dm_reg_r2()

# Define select rule 2
dm_reg_select_r2 = dataset.dm_reg_r1 & ~dataset.dm_reg_r2

# Apply business rules to set population
dataset.set_population(dm_reg_select_r2)

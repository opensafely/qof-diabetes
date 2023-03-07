library(magrittr)
library(dplyr)
library(tidyr)
library(here)
library(readr)
library(fs)
library(purrr)
library(stringr)
library(here)

# Get file names and path
dir_dm_datasets <- fs::dir_ls(path = here("output", "individual_datasets"))

# Load and join all datasets
# Specify column types, this is only needed if one dataset has no data
dm_datasets <- dir_dm_datasets %>%
  purrr::map_dfr(readr::read_csv,
    .id = "id",
    col_types = list(
      patient_id = col_integer(),
      reg_dat = col_date(),
      dereg_dat = col_date(),
      pat_age = col_integer(),
      dm_dat = col_date(),
      dmlat_dat = col_date(),
      dmres_dat = col_date(),
      dmmax_dat = col_date(),
      ifcchba_dat = col_date(),
      ifcchba_val = col_integer(),
      serfruc_dat = col_date(),
      bldtestdec_dat = col_date(),
      dminvite1_dat = col_date(),
      dminvite2_dat = col_date(),
      dmpcadec_dat = col_date(),
      dmpcapu_dat = col_date(),
      modfrail_dat = col_date(),
      sevfrail_dat = col_date(),
      fraillat_dat = col_date(),
      dm_reg_r1 = col_logical(),
      dm_reg_r2 = col_logical(),
      dm020_r1 = col_logical(),
      dm020_r2 = col_logical(),
      dm020_r3 = col_logical(),
      dm020_r4 = col_logical(),
      dm020_r5 = col_logical(),
      dm020_r6 = col_logical(),
      dm020_r7 = col_logical(),
      dm020_r8 = col_logical(),
      dm020_r9 = col_logical(),
      dm020_r10 = col_logical(),
      dm021_r1 = col_logical(),
      dm021_r2 = col_logical(),
      dm021_r3 = col_logical(),
      dm021_r4 = col_logical(),
      dm021_r5 = col_logical(),
      dm021_r6 = col_logical(),
      dm021_r7 = col_logical(),
      dm021_r8 = col_logical(),
      dm021_r9 = col_logical(),
      dm021_r10 = col_logical()
    )
  )

# Check that variable "index_date" doesnt exist yet
if ("index_date" %in% names(dm_datasets)) {
  stop("Variable index_date must not exists in the generated datasets because it get's calculated in the next part of the script.")
}

# Extract indicator and index_date (date) from file name
dm_datasets_tidy <- dm_datasets %>%
  mutate(id = stringr::str_extract(id, "dm\\d{3}_\\d{4}-\\d{2}-\\d{2}")) %>%
  tidyr::separate(id, into = c("indicator", "index_date"), sep = "_") %>%
  mutate(index_date = as.Date(index_date))

# Write dataset
fs::dir_create(here("output", "joined_datasets"))
readr::write_csv(dm_datasets_tidy, here("output", "joined_datasets", "dm_datasets.csv"))

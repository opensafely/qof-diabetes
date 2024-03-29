# This scripts creates dummy data to test the QOF rules
# nolint start: line_length_linter.

# Expected indicators test patients are included in (and specific select rule)
# Patient 1:
# Patient 2: Included in dm017 (r2), dm020 (r2), dm021 (r2)
# Patient 3: Included in dm017 (r2)
# Patient 4:
# Patient 5: Included in dm017 (r2)
# Patient 6:
# Patient 7:
# Patient 8: Included in dm017 (r2), dm020 (r10), dm021 (r10)
# Patient 9:
# Patient 10:
# Patient 11: Included in dm017 (r2), dm021 (r2)

# Addresses
# NOTE: Boolean T and F need to be specified as strings here
addresses <- tibble::tribble(
  ~patient_id, ~address_id,  ~start_date,    ~end_date, ~address_type, ~rural_urban_classification, ~imd_rounded,  ~msoa_code, ~has_postcode, ~care_home_is_potential_match, ~care_home_requires_nursing, ~care_home_does_not_require_nursing,
            1,           1, "1900-01-01",           NA,             1,                           1,        32400, "E02000010",           "T",                           "T",                         "F",                                 "T",
            2,           1, "1950-01-01",           NA,             1,                           1,        22400, "E02000011",           "T",                           "F",                          NA,                                  NA,
            3,           1, "1960-01-01", "2020-01-01",             1,                           1,        12400, "E02000012",           "T",                           "F",                          NA,                                  NA,
            3,           1, "2020-01-02",           NA,             1,                           1,        12400, "E02000013",           "T",                           "T",                         "F",                                 "T",
            4,           1, "1970-01-01",           NA,             1,                           1,         2400, "E02000013",           "T",                           "F",                          NA,                                  NA,
            5,           1, "1980-01-01",           NA,             1,                           1,          400, "E02000014",           "T",                           "F",                          NA,                                  NA,
            6,           1, "1990-01-01",           NA,             1,                           1,         1400, "E02000014",           "T",                           "F",                          NA,                                  NA,
            7,           1, "2000-01-01",           NA,             1,                           1,         2400, "E02000015",           "T",                           "F",                          NA,                                  NA,
            8,           1, "2000-01-01",           NA,             1,                           1,         3400, "E02000015",           "T",                           "F",                          NA,                                  NA,
            9,           1, "2021-01-01",           NA,             1,                           1,         4400, "E02000015",           "T",                           "F",                          NA,                                  NA,
           11,           1, "2000-01-01",           NA,             1,                           1,         4400, "E02000015",           "T",                           "F",                          NA,                                  NA,
  )

readr::write_csv(addresses, here::here("dummy_data", "addresses.csv"), na = "")

# Clinical events
clinical_events <- tibble::tribble(
  ~patient_id,        ~date,    ~snomedct_code, ~ctv3_code, ~numeric_value,
            2, "2018-10-01",         111552007,         NA,             NA,
            2, "2018-11-01",   112991000000101,         NA,             NA,
            2, "2020-05-20",          11530004,         NA,             NA,
            2, "2021-06-01",  1066911000000100,         NA,             NA,
            2, "2021-07-01",  1066921000000106,         NA,             NA,
            2, "2021-08-01",  1066931000000108,         NA,             NA,
            2, "2022-06-01",         127014009,         NA,             NA,
            2, "2022-06-01",         127014009,         NA,             NA,
            2, "2022-06-01",         127014009,         NA,             NA,
            2, "2022-06-01",         127014009,         NA,             NA,
            2, "2022-01-01",   116471000119100,         NA,             NA,
            2, "2022-01-02",         407569005,         NA,             NA,
            2, "2022-01-03",   716031000000106,         NA,             NA,
            2, "2022-02-03",   925791000000100,         NA,             NA,
            2, "2022-01-04",  1049301000000100,         NA,             53,
            2, "2022-01-05",   717421000000100,         NA,             NA,
            2, "2022-01-06",   925791000000100,         NA,             NA,
            2, "2022-01-15",   925861000000102,         NA,             NA,
            2, "2022-02-01",   925831000000107,         NA,             NA,
            2, "2022-01-01",  1006751000000102,         NA,             NA,
            2, "2022-12-01",         315051004,         NA,             NA,

            3, "2022-01-04",  1049301000000100,         NA,             80,
            3, "2019-10-01",     1481000119100,         NA,             NA,
            3, "2019-11-01",         190372001,         NA,             NA,
            3, "2022-02-20",         230577008,         NA,             NA,
            3, "2022-12-01",         237601000,         NA,             NA,
            3, "2017-06-01",  1066911000000100,         NA,             NA,
            3, "2021-06-01",  1066911000000100,         NA,             NA,
            3, "2021-06-04",  1066921000000106,         NA,             NA,
            3, "2021-06-09",  1066921000000106,         NA,             NA,
            3, "2021-07-01",  1066921000000106,         NA,             NA,
            3, "2021-08-01",  1066931000000108,         NA,             NA,
            3, "2020-12-12",         315051004,         NA,             NA,
            3, "2022-02-03",   925791000000100,         NA,             NA,

            4, "2001-12-12",     1481000119100,         NA,             NA,
            4, "2021-01-01",         315051004,         NA,             NA,
            4, "2022-02-03",   925791000000100,         NA,             NA,

            5, "2021-01-01",         190372001,         NA,             NA,

            6, "2000-01-01",         190372001,         NA,             NA,
            6, "2020-12-12",         315051004,         NA,             NA,

            7, "1980-01-01",         190372001,         NA,             NA,
            7, "2020-01-01",         315051004,         NA,             NA,

            8, "2018-10-01",         111552007,         NA,             NA,
            8, "2018-11-01",   112991000000101,         NA,             NA,
            8, "2020-05-20",          11530004,         NA,             NA,
            8, "2021-06-01",  1066911000000100,         NA,             NA,
            8, "2022-06-01",         127014009,         NA,             NA,
            8, "2022-06-01",         127014009,         NA,             NA,
            8, "2022-06-01",         127014009,         NA,             NA,
            8, "2022-06-01",         127014009,         NA,             NA,
            8, "2020-01-01",   116471000119100,         NA,             NA,
            8, "2020-01-02",         407569005,         NA,             NA,
            8, "2020-01-03",   716031000000106,         NA,             NA,
            8, "2022-02-03",   925791000000100,         NA,             NA,
            8, "2022-01-04",  1049301000000100,         NA,             80,
            8, "2020-01-05",   717421000000100,         NA,             NA,
            8, "2022-01-06",   925791000000100,         NA,             NA,
            8, "2022-01-15",   925861000000102,         NA,             NA,
            8, "2022-02-01",   925831000000107,         NA,             NA,
            8, "2022-01-01",  1006751000000102,         NA,             NA,
            8, "2022-12-01",         315051004,         NA,             NA,

           11, "2018-10-01",         111552007,         NA,             NA,
           11, "2018-11-01",   112991000000101,         NA,             NA,
           11, "2020-05-20",          11530004,         NA,             NA,
           11, "2021-06-01",  1066911000000100,         NA,             NA,
           11, "2021-07-01",  1066921000000106,         NA,             NA,
           11, "2022-06-01",         127014009,         NA,             NA,
           11, "2022-06-01",         127014009,         NA,             NA,
           11, "2022-06-01",         127014009,         NA,             NA,
           11, "2022-06-01",         127014009,         NA,             NA,
           11, "2020-01-01",   116471000119100,         NA,             NA,
           11, "2022-01-02",         407569005,         NA,             NA,
           11, "2020-01-03",   716031000000106,         NA,             NA,
           11, "2022-02-03",   925791000000100,         NA,             NA,
           11, "2021-05-04",  1049301000000100,         NA,             74,
           11, "2020-01-05",   717421000000100,         NA,             NA,
           11, "2022-01-06",   925791000000100,         NA,             NA,
           11, "2022-01-15",   925861000000102,         NA,             NA,
           11, "2022-02-01",   925831000000107,         NA,             NA,
           11, "2022-01-01",  1006751000000102,         NA,             NA,
           11, "2022-12-01",         315051004,         NA,             NA,
  )

readr::write_csv(clinical_events, here::here("dummy_data", "clinical_events.csv"), na = "")

# Patients
patients <- tibble::tribble(
  ~patient_id, ~date_of_birth,      ~sex, ~date_of_death,
            1,   "1900-01-01",  "female",             NA,
            2,   "1950-01-01",  "female",   "2022-10-01",
            3,   "1960-01-01",  "female",             NA,
            4,   "1970-01-01",        NA,             NA,
            5,   "1980-01-01",        NA,             NA,
            6,   "1990-01-01", "unknown",             NA,
            7,   "2000-01-01",    "male",             NA,
            8,   "2000-01-01",    "male",             NA,
            9,   "2021-01-01",    "male",             NA,
           10,   "1930-01-01",  "female",   "2022-01-01",
           11,   "2000-01-01",    "male",             NA,
  )

readr::write_csv(patients, here::here("dummy_data", "patients.csv"), na = "")


# Practice registrations
practice_registrations <- tibble::tribble(
  ~patient_id,  ~start_date,    ~end_date, ~practice_pseudo_id, ~practice_stp, ~practice_nuts1_region_name,
            1, "2018-01-01",           NA,                   1,             1,          "region_practice1",
            2, "2010-01-01", "2012-01-01",                   1,             1,          "region_practice1",
            2, "2012-02-01", "2018-01-01",                   2,             1,          "region_practice2",
            2, "2018-01-02",           NA,                   3,             1,          "region_practice3",
            3, "2000-01-01", "2019-01-01",                   2,             2,          "region_practice2",
            3, "2019-02-01", "2023-01-01",                   3,             2,          "region_practice3",
            3, "2023-01-02",           NA,                   4,             2,          "region_practice4",
            4, "2018-01-01",           NA,                   2,             2,          "region_practice2",
            5, "2018-01-01",           NA,                   2,             2,          "region_practice2",
            6, "2018-01-01",           NA,                   3,             3,          "region_practice3",
            7, "2018-01-01",           NA,                   3,             3,          "region_practice3",
            8, "2018-01-01",           NA,                   3,             3,          "region_practice3",
            9, "2018-01-01",           NA,                   3,             3,          "region_practice3",
           10, "2018-01-01",           NA,                   3,             3,          "region_practice3",
           11, "2018-01-01",           NA,                   3,             3,          "region_practice3",
  )

readr::write_csv(practice_registrations, here::here("dummy_data", "practice_registrations.csv"), na = "")
# nolint end

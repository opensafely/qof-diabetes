from datetime import date
from dataset_definition_dm017 import dataset

from ehrql.codes import SNOMEDCTCode

# Patient data for the FY22/23
# Run the tests with the following command:
# opensafely exec ehrql:v0 assure analysis/test_dataset_definition_dm017.py -- 2022-04-01 2023-03-31
patient_data = {
    # Correctly expected in population
    1: {
        "patients": [{"date_of_birth": date(1950, 1, 1)}],
        "practice_registrations": [
            {
                "start_date": date(2010, 1, 1),
                "end_date": date(2018, 1, 1),
                "practice_pseudo_id": 1,
                "practice_stp": 1,
                "practice_nuts1_region_name": "region_practice1",
            },
            {
                "start_date": date(2018, 1, 2),
                "practice_pseudo_id": 3,
                "practice_stp": 3,
                "practice_nuts1_region_name": "region_practice3",
            },
        ],
        "clinical_events": [{}],
        "expected_columns": {
            "reg_dat": date(2018, 1, 2),
            "dereg_dat": None,
            "pat_age": 73,
            "dm_dat": None,
            "dmlat_dat": None,
            "dmres_dat": None,
            "dm_reg_r1": None,
            "dm_reg_r2": False,
            },
    },
    2: {
        "patients": [{"date_of_birth": date(1950, 1, 1)}],
        "practice_registrations": [
            {
                "start_date": date(2019, 2, 1),
                "end_date": None,
                "practice_pseudo_id": 1,
                "practice_stp": 1,
                "practice_nuts1_region_name": "region_practice1",
            },
        ],
        "clinical_events": [
            {
                # First diabetes diagnosis (DM_COD)
                "date": date(2000, 6, 1),
                "snomedct_code": "73211009",
            },
            {
                # Last diabetes diagnosis (DM_COD)
                "date": date(2023, 2, 1),
                "snomedct_code": "73211009",
            },
            {
                # Diabetes diagnosis resolved (DMRES_COD)
                "date": date(2023, 1, 1),
                "snomedct_code": "315051004",
            },
        ],
        "expected_columns": {
            "reg_dat": date(2019, 2, 1),
            "dereg_dat": None,
            "pat_age": 73,
            "dm_dat": date(2000, 6, 1),
            "dmlat_dat": date(2023, 2, 1),
            "dmres_dat": date(2023, 1, 1),
            "dm_reg_r1": True,
            "dm_reg_r2": False,
        },
    },
}

# Quality and Outcomes Framework - Diabetes mellitus

[View on OpenSAFELY](https://jobs.opensafely.org/repo/https%253A%252F%252Fgithub.com%252Fopensafely%252Fqof-diabetes)

Details of the purpose and any published outputs from this project can be found at the link above.

The contents of this repository MUST NOT be considered an accurate or valid representation of the study or its purpose. 
This repository may reflect an incomplete or incorrect analysis with no further ongoing work.
The content has ONLY been made public to support the OpenSAFELY [open science and transparency principles](https://www.opensafely.org/about/#contributing-to-best-practice-around-open-science) and to support the sharing of re-usable code for other subsequent users.
No clinical, policy or safety conclusions must be drawn from the contents of this repository.

## Overview

The study in this repositoy aims to implement the QOF diabetes indicators in OpenSAFELY using [ehrQL (Electronic Health Record Query Language)](https://docs.opensafely.org/ehrql/).

## Repository structure

The following list outlines the the general steps for implementing QOF indicators in OpenSAFELY:

1. All codelists specified in the QOF busieness rules are added to [codelists/codelists.txt](codelists/codelists.txt). 
   The ***codelists*** can be found on OpenCodelists under [NHSD Primary Care Domain Refsets](https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/), see section ***3.2.3 Clinical code clusters*** in the [QOF v46 Business rules](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release).
1. The ***variables*** specified in the business rules (see section ***3.2.4 Clinical data extraction criteria*** in the [QOF v46 Business rules](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release)) are translated into ehrQL and defined in [analysis/dm_dataset.py](analysis/dm_dataset.py).
   The function `make_dm_dataset` takes one argument (`index_date`) and creates a dataset with all variables specified in the business rules in reference to the spcified date.
   The logic of the *business rules* for each indicator are defined in [analysis/dm_dataset.py](analysis/dm_dataset.py) as individual functions (e.g., `get_dm020_r1` specifies rule 1 of indicator DM020) and make use of the variables created by `make_dm_dataset` (see section ***4.1 Indicator(s)*** in the [QOF v46 Business rules](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release)). 
   Rules that are identical across indicators are copied at the end of the script so that the names match (e.g., `get_dm021_r1 = get_dm020_r1`) with each indicator. 
2. The denominator and numerator for each indicator are defined in each dataset definition (e.g., [analysis/dataset_definition_dm020.py](analysis/dataset_definition_dm020.py)). 
   Note that each indicator has it's own dataset definition in the [analysis/](analysis/) subfolder of this repository.

## Parameterisation

For indicators that share identical business rule logic and only differ in cutoff values (e.g., DM020 and DM020) we make use of a feature called parameterisation.
This allows us define the logic that is shared across both indicators once and provide different cutoff values in the [project.yaml](project.yaml) file where we define the actions of this study.

For example, this secion of the [project.yaml](project.yaml) file specifies the action to generate the measures (see below for more information on measures) for indicator DM020. Note that we can specify values that can be accessed in the dataset definitions following `--`, here `--ifcchba-cutoff-val 58`:

```yaml
  generate_measures_dm020:
    run: >
      ehrql:v0 
        generate-measures analysis/dataset_definition_dm020.py
        --dummy-tables dummy_data
        --output output/measures/measures_dm020.csv
        -- 
        --ifcchba-cutoff-val 58
    outputs:
      moderately_sensitive:
        cohort: output/measures/measures_dm020.csv
```

In the dataset definition [analysis/dataset_definition_dm020.py](analysis/dataset_definition_dm020.py) we can now access the cutoff value we specified in the [project.yaml](project.yaml) file using the `argparse` library:

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--ifcchba-cutoff-val", type=int)
args = parser.parse_args()
ifcchba_cutoff_val = args.ifcchba_cutoff_val
```

## Measures

The Measures framework allows us to extract multiple datasets covering different time periods, and calculates a set of measures (here a numerator / denominator pair) for each period.
To use the measures framework we need to use the `generate-measures` action from `ehrql` in the [project.yaml](project.yaml) file.

In our dataset definition (e.g., [analysis/dataset_definition_dm020.py](analysis/dataset_definition_dm020.py)) we specify the numerator and denominator logic from each business rule:

```python
# Define DM020 denominator and numerator
# DM020 gets applied to DM_REG (has_dm_reg_select_r2)
# The numerator is applied to the patients selected into the denominator for this indicator.
dm020_numerator = has_dm020_select_r2
dm020_denominator = has_dm_reg_select_r2 & (has_dm020_select_r2 | has_dm020_select_r10)
```

Now we can define a measures object (`measures = Measures()`) and the numerator and denominator pair as specified in the [QOF v46 Business rules](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/quality-and-outcome-framework-qof-business-rules/qof-business-rules-v46.0-2021-2022-baseline-release) using the `.define_measures()` function:

- `name="dm020"`: String to specify a name (dm020) of the measure
- `numerator` and `denominator`: Variables from the dataset definition that define the measure
- `group_by={"sex": patients.sex}`: In this study we calculate the measure grouped by `sex` column from the `patients` table
- `intervals=months(12).starting_on("2022-03-01")`:  Here we define the intervals that are used the run the dataset definition over a series of dates. In this study we run the dataset definition 12 times monthly starting from 1st March 2022.

```python
# Define measures
measures = Measures()

measures.define_measure(
    name="dm020",
    numerator=dm020_numerator,
    denominator=dm020_denominator,
    group_by={"sex": patients.sex},
    intervals=months(12).starting_on("2022-03-01"),
)
```

This study is set up so that each monthly cohort replicates the yearly reporting of each QOF business rule. 
Thus, the data from March aligns with the reporting period of the corresponding annual QOF reports published by NHS Digital.

## About the OpenSAFELY framework

The OpenSAFELY framework is a Trusted Research Environment (TRE) for electronic
health records research in the NHS, with a focus on public accountability and
research quality.

Read more at [OpenSAFELY.org](https://opensafely.org).

## Licences
As standard, research projects have a MIT license. 

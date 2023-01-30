# qof-diabetes

[View on OpenSAFELY](https://jobs.opensafely.org/repo/https%253A%252F%252Fgithub.com%252Fopensafely%252Fqof-diabetes)

Details of the purpose and any published outputs from this project can be found at the link above.

The contents of this repository MUST NOT be considered an accurate or valid representation of the study or its purpose. 
This repository may reflect an incomplete or incorrect analysis with no further ongoing work.
The content has ONLY been made public to support the OpenSAFELY [open science and transparency principles](https://www.opensafely.org/about/#contributing-to-best-practice-around-open-science) and to support the sharing of re-usable code for other subsequent users.
No clinical, policy or safety conclusions must be drawn from the contents of this repository.

## Overview

The study in this repositoy aims to implement the QOF diabetes indicators DM017, DM020, and DM021 in OpenSAFELY using [ehrQL (Electronic Health Record Query Language)](https://docs.opensafely.org/data-builder/ehrql/).

## Repository structure

The following list outlines the the general steps for implementing QOF indicators in OpenSAFELY:

1. All codelists specified in the QOF busieness rules are added to [codelists/codelists.txt](codelists/codelists.txt). 
   The codelists can be found on OpenCodelists under [NHSD Primary Care Domain Refsets](https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/).
1. The variables specified in the business rules are translated into ehrQL and defined in [analysis/dm_dataset.py](analysis/dm_dataset.py).
   The function `make_dm_dataset` creates a dataset with all variables specified in the business rules.
   The business rules for each indicator are also defined in [analysis/dm_dataset.py](analysis/dm_dataset.py) as individual functions (e.g., `get_dm020_r1` specifies rule 1 of indicator DM020) and make use of the variables created by `make_dm_dataset`. 
   Rules that are identical across indicators are copied at the end of the script so that the names match (e.g., `get_dm021_r1 = get_dm020_r1`) with each indicator. 
1. Denominator rules are defined in each dataset definition (e.g., [analysis/dataset_definition_dm020.py](analysis/dataset_definition_dm020.py)). 
   Note that each indicator has it's own dataset definition.

## About the OpenSAFELY framework

The OpenSAFELY framework is a Trusted Research Environment (TRE) for electronic
health records research in the NHS, with a focus on public accountability and
research quality.

Read more at [OpenSAFELY.org](https://opensafely.org).

## Licences
As standard, research projects have a MIT license. 

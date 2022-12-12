from pathlib import Path

from databuilder.codes import codelist_from_csv

CODELIST_DIR = Path("codelists")

# Cluster name: DM_COD
# Description: Diabetes mellitus codes
# Refset ID: ^999004691000230108
dm_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-dm_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: DMRES_COD
# Description: Diabetes resolved codes
# Refset ID: ^999003371000230102
dm_res_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-dmres_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: DMINVITE_COD
# Description: Invite for diabetes care review codes
# Refset ID: ^999012371000230109
dm_invite_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-dminvite_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: DMMAX_COD
# Description: Codes for maximum tolerated diabetes treatment
# Refset ID: ^999010651000230109
dm_max_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-dmmax_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: DMPCAPU_COD
# Description: Codes for diabetes quality indicator care unsuitable for patient
# Refset ID: ^999010731000230107
dm_pcapu_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-dmpcapu_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: IFCCHBAM_COD
# Description: IFCC HbA1c monitoring range codes
# Refset ID: ^999003251000230103
ifcchbam_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-ifcchbam_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: MILDFRAIL_COD
# Description: Mild frailty diagnosis codes
# Refset ID: ^999013531000230106
mild_frail_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-mildfrail_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: MODFRAIL_COD
# Description: Moderate frailty diagnosis codes
# Refset ID: ^999013571000230108
mod_frail_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-modfrail_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: SERFRUC_COD
# Description: Serum fructosamine codes
# Refset ID: ^999005691000230107
ser_fruc_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-serfruc_cod.csv",
    system="snomedct",
    column="code",
)

# Cluster name: SEVFRAIL_COD
# Description: Severe frailty diagnosis codes
# Refset ID: ^999012131000230109
sev_frail_cod = codelist_from_csv(
    CODELIST_DIR / "nhsd-primary-care-domain-refsets-sevfrail_cod.csv",
    system="snomedct",
    column="code",
)

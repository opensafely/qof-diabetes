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

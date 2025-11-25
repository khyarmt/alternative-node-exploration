import pandas as pd
import settings
from utils import assign_sector_code

dataset_path = settings.dataset_path
yyyymm = "202501"

# import datasets
companies = pd.read_csv(
    f"{dataset_path}/c2/{yyyymm}",
    usecols=["企業CD", "TDB産業分類CD1"],
    dtype={"企業CD": str, "TDB産業分類CD1": str},
).rename(columns={"企業CD": "company_code", "TDB産業分類CD1": "industry_code"})

companies["subsector_code"] = companies["industry_code"].str[:2]
companies["sector_code"] = companies["subsector_code"].apply(
    assign_sector_code
)

print(companies[companies["sector_code"].isna()].head())

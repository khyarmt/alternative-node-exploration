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

trades = pd.read_csv(
    f"{dataset_path}/trd/{yyyymm}",
    usecols=["発注側企業CD", "受注側企業CD"],
    dtype={"発注側企業CD": str, "受注側企業CD": str},
).rename(
    columns={
        "発注側企業CD": "buyer_company_code",
        "受注側企業CD": "seller_company_code",
    }
)
trades = (
    pd.merge(
        trades,
        companies[["company_code", "sector_code"]],
        left_on="buyer_company_code",
        right_on="company_code",
        how="inner",
    )
    .drop(columns=["company_code"])
    .rename(columns={"sector_code": "buyer_sector_code"})
)
trades = (
    pd.merge(
        trades,
        companies[["company_code", "sector_code"]],
        left_on="seller_company_code",
        right_on="company_code",
        how="inner",
    )
    .drop(columns=["company_code"])
    .rename(columns={"sector_code": "seller_sector_code"})
)

# aggregation
# by sector
count_buying_sector = (
    trades[["buyer_company_code", "seller_sector_code", "seller_company_code"]]
    .pivot_table(
        index="buyer_company_code",
        columns="seller_sector_code",
        aggfunc="count",
    )
    .reset_index()
)
count_buying_sector.columns = count_buying_sector.columns.droplevel(0)
count_buying_sector.columns.name = None
count_buying_sector = count_buying_sector.rename(columns={"": "company_code"})
buying_sectors = [
    sector
    for sector in count_buying_sector.columns
    if sector != "company_code"
]
count_buying_sector[buying_sectors] = (
    count_buying_sector[buying_sectors].fillna(0).astype(int)
)
count_buying_sector = count_buying_sector.rename(
    columns={column: f"buy_{column}" for column in buying_sectors}
)
print(count_buying_sector.head())

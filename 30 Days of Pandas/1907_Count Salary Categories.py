# %%
import pandas as pd
import numpy as np

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=["account_id", "income"]).astype(
    {"account_id": "Int64", "income": "Int64"}
)


# %%
accounts["income_category"] = pd.cut(
    accounts["income"],
    bins=[0, 20000, 50001, np.inf],
    labels=["Low Salary", "Average Salary", "High Salary"],
    right=False,
)

accounts.groupby("income_category").count().reset_index()[
    ["income_category", "account_id"]
].rename(
    columns={"account_id": "accounts_count", "income_category": "category"}
).sort_values(
    by="accounts_count", ascending=False
)

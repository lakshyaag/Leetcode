# %%
import pandas as pd

data = [[1, "aLice"], [2, "bOB"]]
users = pd.DataFrame(data, columns=["user_id", "name"]).astype(
    {"user_id": "Int64", "name": "object"}
)

# %%
users["name"] = users["name"].apply(lambda x: x[0].upper() + x[1:].lower())
users.sort_values(by="user_id")

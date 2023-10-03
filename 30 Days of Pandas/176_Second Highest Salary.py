# %%
import pandas as pd

data = [[1, 100]]
employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
    {"id": "int64", "salary": "int64"}
)

# %%
salaries = employee.sort_values(by="salary", ascending=False).drop_duplicates()

salaries.iloc[1] if len(salaries) >= 2 else None

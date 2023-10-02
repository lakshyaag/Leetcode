# %%
import pandas as pd

data = [[1, 100]]
employee = pd.DataFrame(data, columns=["id", "salary"]).astype(
    {"id": "Int64", "salary": "Int64"}
)

N = 1

salaries = (
    employee.sort_values(by="salary", ascending=False)
    .rename(columns={"salary": f"getNthHighestSalary({N})"})[
        [f"getNthHighestSalary({N})"]
    ]
    .drop_duplicates()
)

salaries.iloc[N - 1 : N] if len(salaries) >= N else None

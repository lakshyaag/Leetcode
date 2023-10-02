# %%
import pandas as pd

data = [
    [2, "Meir", 3000],
    [3, "Michael", 3800],
    [7, "Addilyn", 7400],
    [8, "Juan", 6100],
    [9, "Kannon", 7700],
]
employees = pd.DataFrame(data, columns=["employee_id", "name", "salary"]).astype(
    {"employee_id": "int64", "name": "object", "salary": "int64"}
)

employees["bonus"] = 0

employees.loc[
    (employees["employee_id"] % 2 != 0) & (employees["name"].str[0] != "M"), "bonus"
] = (employees["salary"] * 1)

employees.sort_values(by="employee_id")[["employee_id", "bonus"]]

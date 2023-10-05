# %%
import pandas as pd

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=["teacher_id", "subject_id", "dept_id"]).astype(
    {"teacher_id": "Int64", "subject_id": "Int64", "dept_id": "Int64"}
)

teacher

# %%
teacher.groupby("teacher_id").agg({"subject_id": "nunique"}).rename(
    columns={"subject_id": "cnt"}
).reset_index()

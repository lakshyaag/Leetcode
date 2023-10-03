# %%
import pandas as pd
import re

data = [
    [1, "Daniel", "YFEV COUGH"],
    [2, "Alice", ""],
    [3, "Bob", "DIAB100 MYOP"],
    [4, "George", "ACNE DIAB100"],
    [5, "Alain", "DIAB201"],
]
patients = pd.DataFrame(
    data, columns=["patient_id", "patient_name", "conditions"]
).astype({"patient_id": "int64", "patient_name": "object", "conditions": "object"})

# %%
patients.loc[
    patients["conditions"].apply(lambda x: re.search(r"\bDIAB1.", x) is not None)
]

# %%
import pandas as pd

customers = pd.DataFrame(
    {
        "id": [1, 2, 3, 4],
        "name": ["Joe", "Henry", "Sam", "Max"],
    }
)

orders = pd.DataFrame(
    {
        "id": [1, 2],
        "customerId": [3, 1],
    }
)

customers.query("id not in @orders.customerId").rename(columns={"name": "Customers"})[
    ["Customers"]
]

# %%

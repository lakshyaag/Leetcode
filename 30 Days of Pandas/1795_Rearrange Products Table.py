# %%
import pandas as pd

data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=["product_id", "store1", "store2", "store3"])

products

# %%
products.melt(id_vars=["product_id"], var_name="store", value_name="price").dropna()

# %%
import pandas as pd

products = pd.DataFrame(
    {
        "product_id": [0, 1, 2, 3, 4],
        "low_fats": ["Y", "Y", "N", "Y", "N"],
        "recyclable": ["N", "Y", "Y", "Y", "N"],
    }
)

products.query("low_fats == 'Y' & recyclable == 'Y'")[["product_id"]]

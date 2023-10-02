# %%
import pandas as pd
from io import StringIO

input_df = """
name, continent,area,population,gdp
Afghanistan,Asia,652230,25500100,20343000000
Albania,Europe,28748,2831741,12960000000
Algeria,Africa,2381741,37100000,188681000000
Andorra,Europe,468,78115,3712000000
Angola,Africa,1246700,20609294,100990000000
"""

# Read as dataframe
world = pd.read_csv(StringIO(input_df), sep=",")

world.query("area >= 3000000 | population >= 25000000")[["name", "area", "population"]]

import plotly.express as px
import pandas as pd
import numpy as np


df = px.data.iris()

df2 = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"]).cumsum()
df2["A"] = pd.Series(list(range(len(df))))
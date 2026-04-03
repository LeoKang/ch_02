import pandas as pd
from step_2_2 import OUT_2_2

df_raw = pd.read_excel(OUT_2_2)
df_pivot_1 = pd.pivot_table(df_raw, index="분류", values="사용금액", aggfunc="sum")
df_pivot_1
import pandas as pd

df = pd.read_csv("sales_data.csv")

df_sum_total_revenue = df.agg({"Total Revenue": "sum"})

print(df_sum_total_revenue)

df_mean_total_revenue = df.agg({"Total Revenue": "mean"})

print(df_mean_total_revenue)


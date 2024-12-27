import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

df["mean_grade"] = df.iloc[:, 1:].mean(axis=1)

sorted_data = df.sort_values(by="mean_grade", ascending=False)

print(sorted_data.head())


import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import warnings
warnings.filterwarnings(action="ignore")

df = pd.read_csv("births.csv")

df.coloumns

df.head()

#Question___1
df["decade"] = (df["year"] // 10) * 10

#Question___2
df.describe()

df.info()

#Question___3
df.isna().sum()

#Question___4
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="decade", y="births", hue="gender", hue_order=['M', 'F'], ci=False)
plt.xlabel("Decade")
plt.ylabel("Births")
plt.title("Trend of M & F births every decade")

#Question___5
mean_value = df.births.mean()
std_value = df.biths.std()

l_bound = mean_value-5 * std_value
u_bound = mean_value+5 * std_value

df_no_outliers = df[(df["births"]>=l_bound) & (df["births"]<=u_bound)]

rows_removed = df.shape[0] - df_no_outliers.shape[0]
print(f"Number of Rows Removed: {rows_removed}")

#Question___7
month_d = df.groupby("month")["births"].sum().reset_index()
day_d = df.groupby("day")["births"].sum().reset_index()
daily_d = df.groupby(["month", "day"])["births"].sum().reset_index()

print(month_d,"\n", day_d, "\n", daily_d)

#Question___8
avg_birth_rate = df.groupby(["month", "day"])["births"].mean().reset_index()
print(avg_birth_rate)

 
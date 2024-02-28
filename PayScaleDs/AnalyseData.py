import pandas as pd

df=pd.read_csv("Data_of_PayScale.csv")
# print(df.info())
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)

# df.isna()
df["% High Meaning"].idxmax()
df["% High Meaning"][12]
df["Early Career Pay"]=df["Early Career Pay"].str.replace("$","").str.replace(",","").astype("float")
df["Mid-Career Pay"]=df["Mid-Career Pay"].str.replace("$","").str.replace(",","").astype("float")
spread_data=df["Early Career Pay"].subtract(df["Mid-Career Pay"])
df.insert(5,"Spread",spread_data)
df.sort_values("Spread")
# df.groupby("Rank").mean()
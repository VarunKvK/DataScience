import pandas as pd

df=pd.read_csv("QueryResults.csv",names=["Date","Language","Posts"],header=0)
df.shape
df
cleansed_data=df.dropna()
cleansed_data.groupby("Language").sum().max()
cleansed_data.count()
cleansed_data.Date=pd.to_datetime(cleansed_data.Date)
cleansed_data.head()
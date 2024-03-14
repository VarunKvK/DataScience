import pandas as pd

app_df=pd.read_csv("apps.csv")
app_df.head()
app_df.count
app_df.count()
app_df.shape

app_df.sample(5)
app_df.drop(columns=["Last_Updated","Android_Ver"],axis=1,inplace=True)
app_df.head()
app_df.shape

df=app_df.dropna()
df[df.duplicated()]
df=df.drop_duplicates(subset=["App","Type","Price"])
df[df.App=="Instagram"]
df.shape

df.sort_values("Rating",ascending=False).head()
df.sort_values("Size_MBs",ascending=False).head()
df.sort_values("Reviews",ascending=False).head(50)
import pandas as pd
import plotly.express as px

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

ratings=df.Content_Rating.value_counts()
ratings

fig=px.pie(labels=ratings.index,values=ratings.values, title="Content Rating", names=ratings.index, hole=0.6)
fig.update_traces(textposition="outside",textinfo="percent+label")
fig

df.head(2)
df.Installs.value_counts()
df.Installs.describe()
df.info()

df.Installs=df.Installs.astype(str).str.replace(",","")
df.Installs=pd.to_numeric(df.Installs)
df.Installs.describe()
df[["App","Installs"]].groupby("Installs").count()


df.head(1)
df.Price=df.Price.astype(str).str.replace("$","")
df.Price=pd.to_numeric(df.Price)
df.Price.describe()
df[["App","Price"]].groupby("Price").count().sort_values("Price",ascending=False).head(20)


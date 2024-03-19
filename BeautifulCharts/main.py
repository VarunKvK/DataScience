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
df.sort_values("Price",ascending=False).head(20)

df=df[df["Price"]<250]
df.sort_values("Price",ascending=False).head(20)

df["Revenue_Estimate"]=df.Installs.mul(df.Price)
df.sort_values("Revenue_Estimate",ascending=False).head(10)

# df.Category.nunique

top_10=df.Category.value_counts().head(10)
top_10
bar_chart=px.bar(x=top_10.index,y=top_10.values)
bar_chart.show()

category_installs=df.groupby("Category").agg({"Installs":pd.Series.sum})
category_installs.sort_values("Installs",ascending=False,inplace=True)
category_installs.head(10)
category_plot=px.bar(x=category_installs.Installs, y=category_installs.index,orientation='h',title="Category Installs")
category_plot.update_layout(xaxis_title="Installs",yaxis_title="Category")

number_installs=df.groupby("Category").agg({"App":pd.Series.count})
number_installs.head(10)
category_apps=pd.merge(number_installs,category_installs,on="Category",how="inner")
category_apps.head(10)
category_apps.sort_values("App",ascending=True,inplace=True)
scatter=px.scatter(category_apps,x="App",y="Installs",title="Category based on app downlads",size="Installs",hover_name=category_apps.index,color="Installs")
scatter.show()

df.groupby("Genres").describe()
len(df.groupby("Genres").nunique())
df.Genres.value_counts().sort_values(ascending=True)[:5]
stack=df.Genres.str.split(";",expand=True).stack()
num_genres=stack.value_counts()
num_genres

num_genre_bar= px.bar(x=num_genres.index[:15],y=num_genres.values[:15],orientation='v',title="Top Genres",hover_name=num_genres.values[:15],color=num_genres.values[:15],color_continuous_scale='tealrose')
num_genre_bar.update_layout(xaxis_title="Genres",yaxis_title="Number of Apps")
num_genre_bar.show()

#df.Types
df.Type.value_counts()
df_free_vs_paid=df.groupby(['Category',"Type"],as_index=False).agg({'App':pd.Series.count})
df_free_vs_paid

free_vs_paid_chart=px.bar(df_free_vs_paid[:15],x="Category",y="App",title="Free vs Paid", barmode='group',color="Type")
free_vs_paid_chart.update_layout(xaxis_title="App", yaxis_title="Category")
free_vs_paid_chart
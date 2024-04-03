import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data=pd.read_csv("./cost_revenue_dirty.csv")
data.shape
len(data)
data.isna().values.any()
data.duplicated().values.any()
data.info()

# data.USD_Production_Budget=data.USD_Production_Budget.str.replace('$'," ").str.replace(",","").astype("int")
# data.USD_Worldwide_Gross=data.USD_Worldwide_Gross.str.replace('$'," ").str.replace(",","").astype("float")
# data.USD_Domestic_Gross=data.USD_Domestic_Gross.str.replace('$'," ").str.replace(",","").astype("int")
# data.USD_Worldwide_Gross.head(1)

data.Release_Date=pd.to_datetime(data.Release_Date)

char_to_remove=[',','$']
col_to_clean=['USD_Production_Budget','USD_Worldwide_Gross','USD_Domestic_Gross']

for col in col_to_clean:
    for char in char_to_remove:
        data[col]=data[col].str.replace(char,"")
    data[col]=pd.to_numeric(data[col])
    
data.head(1).info()
data.describe()
data.USD_Production_Budget.describe()

data[data.USD_Production_Budget==1100]
data[data.USD_Production_Budget==425000000]


zero_income=data[data.USD_Worldwide_Gross==0]
zero_income.sort_values("USD_Production_Budget",ascending=False)

international_revenue=data[(data.USD_Worldwide_Gross != 0) & (data.USD_Domestic_Gross == 0)]
international_revenue

df_filter=data.query('USD_Worldwide_Gross !=0 and USD_Domestic_Gross==0')
len(df_filter)

time_stamp=pd.Timestamp('2018-05-01')
unreleased_movies=data[data.Release_Date >=time_stamp]
unreleased_movies.sort_values('Release_Date',ascending=False)
len(unreleased_movies)

data_clean=data.drop(unreleased_movies.index)
data_clean.head()
len(data_clean)
data_clean.describe()

money_loss=data_clean[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
(len(money_loss)/len(data_clean))*100

plt.figure(figsize=(8,4))
ax=sns.scatterplot(data=data_clean,x="USD_Production_Budget",y="USD_Worldwide_Gross",hue="USD_Worldwide_Gross",size="USD_Worldwide_Gross")
ax.set(ylim=(0,3000000000),xlim=(0,450000000),xlabel="Budget in $100 billion",ylabel="Revenue in million")
plt.show()

plt.figure(figsize=(8,4),dpi=200)
with sns.axes_style("darkgrid"):
    ax=sns.scatterplot(data=data_clean,x="Release_Date",y="USD_Production_Budget",hue="USD_Worldwide_Gross",size="USD_Worldwide_Gross")
    ax.set(xlim=(data_clean.Release_Date.min,data_clean.Release_Date.max),ylim=(0,450000000),xlabel="TimePeriod",ylabel="USD_Production_Budget")
plt.show()

released_year=pd.DatetimeIndex(data_clean.Release_Date)
years=released_year.year

date_time=years//10*10
data_clean['Decade']=date_time

old_movies=data_clean[data_clean.Decade < 1970]
new_movies=data_clean[data_clean.Decade >= 1970]

old_movies.sort_values("Release_Date",ascending=False).head()
old_movies.describe()
old_movies.sort_values("USD_Production_Budget",ascending=False).head()
new_movies.describe()
new_movies.sort_values("USD_Production_Budget",ascending=False).head()

plt.figure(figsize=(8,14),dpi=120)

with sns.axes_style("whitegrid"):
    sns.regplot(data=old_movies,x="USD_Production_Budget",y="USD_Worldwide_Gross",scatter_kws={'alpha':0.4},line_kws={"color":'red'})
    sns.show()
    

plt.figure(figsize=(8,10),dpi=120)
with sns.axes_style('darkgrid'):
    ax=sns.regplot(data=new_movies,x="USD_Production_Budget", y="USD_Worldwide_Gross",color="#2f4b7c",scatter_kws={'alpha':0.4},line_kws={"color":"#ff7c43"})
    ax.set(xlim=(0,450000000),ylim=(0,3000000000),xlabel="Revenue in $Millions",ylabel="Revenue in $Billions")

regression=LinearRegression()

X=pd.DataFrame(new_movies,columns=['USD_Production_Budget'])
y=pd.DataFrame(new_movies,columns=['USD_Worldwide_Gross'])

regression.fit(X,y)
regression.intercept_
regression.coef_

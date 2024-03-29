import pandas as pd

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
len(data_clean)
data_clean.describe()

money_loss=data_clean[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
(len(money_loss)/len(data_clean))*100
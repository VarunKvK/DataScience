import pandas as pd
import matplotlib.pyplot as plt

############ TSLA DATASET ############
tesla_df=pd.read_csv("Tesla.csv")
tesla_df
tesla_df_month=pd.to_datetime(tesla_df.MONTH)
tesla_df_month

# tesla_df.head()
# tesla_df.shape
# tesla_df.count()
# tesla_df.TSLA_WEB_SEARCH.max()
# tesla_df.TSLA_WEB_SEARCH.min()
# tesla_df.describe()
# tesla_df.columns
# tesla_df.isna().values.any()

# #Clean the data
# c_tsla_df=tesla_df.isna()
# c_tsla_df=tesla_df.dropna()
# c_tsla_df.count

#Line chart 
plt.figure(figsize=(14,8),dpi=120)
plt.title("TeslaPrices vs Search",fontsize=18)

ax1=plt.gca()
ax2=ax1.twinx()

ax1.plot(tesla_df.MONTH, tesla_df.TSLA_WEB_SEARCH, color="blue")
ax2.plot(tesla_df.MONTH, tesla_df.TSLA_USD_CLOSE, color="red")

ax1.set_xlabel("Year")
ax1.set_ylabel("TSLA_WEB_SEARCH",fontsize=14)
ax2.set_ylabel("TSLA_USD_CLOSE",fontsize=14)

plt.show()

plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
 
ax1.plot(tesla_df.MONTH, tesla_df.TSLA_WEB_SEARCH, color="blue")
ax2.plot(tesla_df.MONTH, tesla_df.TSLA_USD_CLOSE, color="red")

 
plt.show()

####################################

############ UE DATASET ############
# ue_df=pd.read_csv("UE Benefits Search vs UE Rate 2004-19.csv")

# ue_df_month=pd.to_datetime(ue_df.MONTH)
# ue_df_month

# ue_df.head()
# ue_df.shape
# ue_df.count()
# ue_df.count
# ue_df.UE_BENEFITS_WEB_SEARCH.max()
# ue_df.UE_BENEFITS_WEB_SEARCH.min()
# ue_df.describe()
# ue_df.columns
# ue_df.isna().values.any()

# #Clean the data
# c_ue_df=ue_df.dropna()
# c_ue_df.count
# ####################################

# ############ BITCOIN SEARCH DATASET ############
# btc_df=pd.read_csv("Bitcoin Search Trend.csv")
# type(btc_df.MONTH[0])

# btc_df_month=pd.to_datetime(btc_df.MONTH)
# btc_df_month.head()

# btc_df.head()
# btc_df.shape
# btc_df.count()
# btc_df.count
# btc_df.BTC_NEWS_SEARCH.max()
# btc_df.BTC_NEWS_SEARCH.min()
# btc_df.describe()
# btc_df.columns
# btc_df.isna().values.any()

# #Clean the data
# c_btc_df=btc_df.dropna()
# c_btc_df.count
# ####################################

# ############ BITCOIN DATASET ############
# btc_p_df=pd.read_csv("Daily Bitcoin Price.csv")
# btc_p_df.DATE=pd.to_datetime(btc_p_df.DATE)
# btc_p_df.set_index('DATE', inplace=True)
# btc_monthly_df=btc_p_df.resample("ME").last()
# btc_monthly_df_mean=btc_p_df.resample("ME").mean()
# btc_monthly_df
# btc_monthly_df_mean

# btc_p_df.head()
# btc_p_df.shape
# btc_p_df.count()
# btc_p_df.count
# btc_p_df.CLOSE.max()
# btc_p_df.CLOSE.min()
# btc_p_df.describe()
# btc_p_df.columns
# btc_p_df.isna().values.any()
# btc_p_df.isna().values.any().sum()
# btc_p_df[btc_p_df.CLOSE.isna()]

# #Clean the data
# c_btc_p_df=btc_p_df.dropna(inplace=True)
# c_btc_p_df.count
# ####################################
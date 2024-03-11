import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as d

bitcoin_df=pd.read_csv("Daily Bitcoin Price.csv")
bitcoin_df_search=pd.read_csv("Bitcoin Search Trend.csv")
# bitcoin_df.rename(columns={"DATE":"MONTH"},inplace=True)

# bitcoin_df.isna().values.any()
# bitcoin_df.isna().values.sum()
# bitcoin_df[bitcoin_df.CLOSE.isna()]
# bitcoin_df.dropna(inplace=True)

bitcoin_df.DATE=pd.to_datetime(bitcoin_df.DATE)
bitcoin_df_search.DATE=pd.to_datetime(bitcoin_df_search.MONTH)

bitcoin_df.set_index('DATE', inplace=True)
bitcoin_df_search.set_index('MONTH', inplace=True)



bitcoin_df_monthly=bitcoin_df.resample("ME").first()

print(bitcoin_df_monthly.shape)
bitcoin_df.head()



plt.figure(figsize=(14,8),dpi=120)
plt.title("Bitcoin Price Analysis")
ax1=plt.gca()
ax2=ax1.twinx()

year_locator=d.YearLocator()
month_locator=d.MonthLocator()
year_formatter=d.DateFormatter("%Y-%m")

ax1.xaxis.set_major_locator(year_locator)
ax1.xaxis.set_minor_locator(month_locator)
ax1.xaxis.set_major_formatter(year_formatter)

# ax1.set_ylim(bottom=0, top=15000)
# ax1.set_xlim([bitcoin_df.index.min(), bitcoin_df.index.max()])

ax1.plot(bitcoin_df_monthly.index,bitcoin_df_monthly.CLOSE, label="Bitcoin CLOSE", color="green", marker="o")
ax2.plot(bitcoin_df_monthly.index,bitcoin_df_search.BTC_NEWS_SEARCH, label="Bitcoin SEARCH", color="blue", linestyle="--")

ax1.set_ylabel("Bitcoin CLOSE",fontsize=14,color="green")
ax2.set_ylabel("Bitcoin SEARCH",fontsize=14,color="blue")


plt.show()
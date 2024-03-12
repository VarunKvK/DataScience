import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md

########## Read the data ##########
ue_data=pd.read_csv("./UE Benefits Search vs UE Rate 2004-19.csv")
# ue_data.head()
# ue_data.shape
ue_data.MONTH=pd.to_datetime(ue_data.MONTH)
ue_data.set_index('MONTH', inplace=True)
# type(ue_data_date)

ue_data.isna().values.any()
ue_data.isna().values.sum()
ue_data=ue_data.dropna()


ue_data_monthy=ue_data.resample("ME").last()
ue_data_monthy.head()

########### Plot the data ##########
plt.figure(figsize=(18,6))
ax1=plt.gca()
ax2=ax1.twinx()

year_locator=md.YearLocator()
month_locator=md.MonthLocator()
year_format=md.DateFormatter("%Y-%m")

ax1.xaxis.set_major_locator(year_locator)
ax1.xaxis.set_minor_locator(month_locator)
ax1.xaxis.set_major_formatter(year_format)

ax1.grid(color="grey", linestyle="--")

roll_data=ue_data_monthy[['UE_BENEFITS_WEB_SEARCH','UNRATE']].rolling(window=6).mean()


# ax1.plot(ue_data_monthy.index, ue_data_monthy.UE_BENEFITS_WEB_SEARCH, color="blue", label="WEB_SEARCH", linewidth="2")
# ax2.plot(ue_data_monthy.index, ue_data_monthy.UNRATE, color="red", label="UNRATE",linewidth="2")
ax1.plot(ue_data_monthy.index, roll_data.UE_BENEFITS_WEB_SEARCH, color="blue", label="WEB_SEARCH", linewidth="2")
ax2.plot(ue_data_monthy.index, roll_data.UNRATE, color="red", label="UNRATE",linewidth="2")

ax1.set_ylabel("WEB_SEARCH",fontsize=14,color="blue")
ax2.set_ylabel("UNRATE",fontsize=14,color="red")
plt.show()


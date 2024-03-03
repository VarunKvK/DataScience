import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("QueryResults.csv",names=["Date","Language","Posts"],header=0)
df.shape
df
cleansed_data=df.dropna()
cleansed_data.groupby("Language").sum().idxmax()
cleansed_data.count
cleansed_data.Date=pd.to_datetime(cleansed_data.Date)
cleansed_data.head()

reshaped_df=cleansed_data.pivot(index="Date",columns="Language", values="Posts")
reshaped_df.head()
reshaped_df.count()
reshaped_df.shape
reshaped_df.columns
reshaped_df.fillna(0,inplace=True)
rolled_df=reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(10,8))
# plt.plot(reshaped_df.index,reshaped_df.java,reshaped_df.python)
for column in rolled_df.columns:
    plt.plot(rolled_df.index,rolled_df[column],label=rolled_df[column].name,linewidth=1)
plt.legend(fontsize=12)
plt.xlabel("Date")
plt.ylabel("Posts")
plt.show
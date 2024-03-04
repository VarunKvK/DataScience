import pandas as pd 
import matplotlib.pyplot as plt


#LEgo Color Datset
color_df=pd.read_csv("colors.csv")
color_df["name"].nunique()
color_df.head()
color_df.groupby("is_trans").count()
color_df.is_trans.value_counts()

#Lego Sets DataSets
set_df=pd.read_csv("sets.csv")
set_df.head()
set_df.count()
set_df.sort_values("year")
set_df[set_df.year==1949]
set_df.sort_values("num_parts",ascending=False).head()
##This 
set_year=set_df.groupby("year").count()
set_year.num_parts.head()

#Plotting Graph using matplot
plt.figure(figsize=(8,6))
plt.plot(set_year.index[:-2],set_year.set_num[:-2])


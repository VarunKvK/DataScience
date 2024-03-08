import pandas as pd 
import matplotlib.pyplot as plt


#Lego Color Datset ################################################################
color_df=pd.read_csv("colors.csv")
color_df["name"].nunique()
color_df.head()
color_df.groupby("is_trans").count()
color_df.is_trans.value_counts()

#Lego Sets DataSets ################################################################
set_df=pd.read_csv("sets.csv")
set_df.head()
set_df.count()
set_df.sort_values("year")
set_df[set_df.year==1949]
set_df.sort_values("num_parts",ascending=False).head()
set_year=set_df.groupby("year").count()
set_year.num_parts.head()

theme_year=set_df.groupby("year").agg({"theme_id":pd.Series.nunique})
theme_year.rename(columns={"theme_id":"nr_theme"},inplace=True)
theme_year


#Plotting Graph using matplot
plt.figure(figsize=(8,6))
ax1=plt.gca()
ax2=ax1.twinx()
ax1.plot(set_year.index[:-2],set_year.set_num[:-2],color="blue")
ax2.plot(theme_year.index[:-2],theme_year.nr_theme[:-2],color="green")

ax1.set_xlabel("Year")
ax1.set_ylabel("Sets",color="blue")
ax2.set_ylabel("Themes",color="green")

#Scatter Plotting
avg_parts=set_df.groupby("year").agg({"num_parts":pd.Series.mean})
parts_avg=avg_parts.rename(columns={"num_parts":"avg"})
parts_avg.head()
parts_avg.tail()

plt.figure(figsize=(10,6))
plt.xlabel("Number of parts")
plt.scatter(parts_avg.index[:-2],parts_avg.avg[:-2])

#Lego Theme Dataset ################################################################
theme_df=pd.read_csv("themes.csv")
clean_theme=theme_df.dropna()
clean_theme.count()


#Relational Database Scheme

#setdata
theme_data=set_df["theme_id"].value_counts()
theme_data=pd.DataFrame({'id':theme_data.index, 'theme_count':theme_data.values})
theme_data.head()

#themedata
theme_data[:5]
clean_theme[clean_theme.name== "Star Wars"] 
set_df[set_df.theme_id==18]

merege_data=pd.merge(theme_data,theme_df,on="id")
merege_data=pd.merge(theme_data,clean_theme,on="id")
merege_data.head()

#BarChart
plt.figure(figsize=(10,6))
plt.bar(merege_data.name[:10],merege_data.theme_count[:10])
plt.xlabel("ThemeCount",fontsize=14)
plt.xticks(fontsize=14,rotation=90)
plt.ylabel("Id",fontsize=14)
plt.show()
from bs4 import BeautifulSoup
import requests
import pandas as pd

#----------------------------------------
#Code for scraping data from the database
#----------------------------------------

response=requests.get('https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')
soup=BeautifulSoup(response.content,'html.parser')

table=soup.find(name="table",class_="data-table")

rows=table.find_all('tr')
table_data=[]
#Login for cleaning the data
for row in rows:
    cells=row.find_all('td')
    column_headers = [th.text.strip() for th in rows[0].find_all('th')]
    # print([cell.text.strip() for cell in cells])
    table_data.append([cell.text.strip() for cell in cells])
    
# Creating an excel file
df=pd.DataFrame(table_data[1:],columns=column_headers)
df = df.map(lambda x: x.split(":")[-1])

# excel_data=df.to_csv("Data of PayScale.csv",index=False)


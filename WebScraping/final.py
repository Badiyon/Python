import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/country/us/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table1 = soup.find('table', id='usa_table_countries_today')
#print(table1)

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

headers[13] = 'Tests/1M pop'

mydata = pd.DataFrame(columns = headers)

for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    row[13] = 0
    row[14] = 0
    length = len(mydata)
    mydata.loc[length] = row
    print(length)
    if (int(length) == 63):
        print('time to break')
        break

del mydata['Projections']
del mydata['Tests/1M pop']



#/html/body/div[4]/div[1]/div/div[5]/div[1]/div/table/tbody[1]/tr[1]/td[13]
#/html/body/div[4]/div[1]/div/div[5]/div[1]/div/table/tbody[1]/tr[1]/td[2]

mydata.drop('#', inplace=True, axis=1)

mydata.to_csv('usa_covid_data.csv', index=False)
mydata2 = pd.read_csv('usa_covid_data.csv')
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table1 = soup.find('table', id='main_table_countries_today')
print(table1)

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

headers[13] = 'Tests/1M pop'

mydata = pd.DataFrame(columns = headers)

for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    print(row[21])
    length = len(mydata)
    mydata.loc[length] = row

mydata.drop(mydata.index[0:7], inplace=True)
mydata.drop(mydata.index[222:229], inplace=True)
mydata.reset_index(inplace=True, drop=True)

mydata.drop('#', inplace=True, axis=1)

mydata.to_csv('covid_data.csv', index=False)
mydata2 = pd.read_csv('covid_data.csv')
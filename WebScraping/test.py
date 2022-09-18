#NAME:Bryan Berkey
#DATE:09/04/2022
#PURPOSE/USE: test out basics of web scraping in python to further my knowledge on it and then develop an application
# that will utilize it in grabbing data from a webpage and transfering that information to an excel document.
#CHANGES:
#

#FIRST NEED TO LEARN WHAT IMPORTS ARE NEEDED AND TEST IT ON A PAGE.

#import requests
#response = requests.get("https://www.worldometers.info/coronavirus/country/us/")
#print(response.text)

#response = requests.get("/html/body/div[4]/div[1]/div/div[5]/div[1]/div/table/tbody[1]/tr[2]")
#print(response.text)

from lxml import html
import requests
page = requests.get('https://en.wikipedia.org/wiki/Outline_of_the_Marvel_Cinematic_Universe')
test = html.fromstring(page.content)

junk = test.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/tbody/tr[*]/th/i/a')

print(junk[1].text)


page1 = requests.get('https://www.worldometers.info/coronavirus/country/us/')
test1 = html.fromstring(page1.content)

junk1 = test.xpath('/html/body/div[4]/div[1]/div/div[5]/div[1]/div/table/tbody[1]/tr[4]/td[3]')
print(junk1.tag)


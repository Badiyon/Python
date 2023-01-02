import requests
import json

#just a testing environment to get familiar with the openweathermap api calls

api_key = ""

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = ""

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()
y = x['main']
z = x['weather'][0]
a = x['wind']['speed']

print(a)
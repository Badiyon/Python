import requests
import json
import weatheremail
import time

#track temp, weather, winds
#
#temp: 'main' => 'temp' (in kelvin translate to F)
#weather: 'weather'[0] => ['description']
#winds: 'wind' => 'speed' (translate from m/s to mph)

def checkTemp(temp):
    if(temp > 90.0 or temp <= 0.0):
        return True
    else:
        return False


def checkWeather(weatherID):
    #see weather ID codes at: https://openweathermap.org/weather-conditions

    if(checkThunderStorm(weatherID) or checkRain(weatherID) or checkSnow(weatherID)):
        return True
    else:
        return False

def checkThunderStorm(ID):
    if(ID == 201 or ID == 212 or ID == 221 or ID == 232):
        return True
    else:
        return False

def checkRain(ID):
    if(ID == 502 or ID == 503 or ID == 504 or ID == 504 or ID == 511 or ID == 522):
        return True
    else:
        return False

def checkSnow(ID):
    if(ID == 602 or ID == 613 or ID == 616 or ID == 621 or ID == 622):
        return True
    else:
        return False


def checkWind(wind):

    if(wind > 35.0):
        return True
    else:
        return False



def fahrTemp(kTemp):
    return round( ((float(kTemp) * (9/5)) - 459.67), 2)

def mphWind(msWind):
    return round( (float(msWind) * 2.236936), 2)


#some api and location information have been left blank since I do not want to
#publish some of this information on GitHub
def callOpenWeatherAPI():
    api_key = ""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ""
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    x = response.json()

    return x


def main():
    while(True):
        API_INFO = callOpenWeatherAPI()

        temp = fahrTemp(API_INFO['main']['temp'])
        weatherID = int(API_INFO['weather'][0]['id'])
        wind = mphWind(API_INFO['wind']['speed'])



        if(checkTemp(temp) or checkWeather(weatherID) or checkWind(wind)):
            weatheremail.sendMail()
            time.sleep(28800)

        time.sleep(3600)



if __name__ == "__main__":
    main()


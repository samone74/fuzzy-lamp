import requests
import json

api_key = "3f8b55140932f78771bfaf2c85840b0b"
lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
# response = requests.get(url)
# data = json.loads(response.text)
# print(data)

import pyowm

APIKEY = '3f8b55140932f78771bfaf2c85840b0b'  # your API Key here as string
owm = pyowm.OWM(APIKEY)  # Use API key to get data
mgr = owm.weather_manager()
Weather = mgr.weather_at_place('Nootdorp')  # give where you need to see the weather
w = Weather.weather

print(w.detailed_status)  # 'clouds'
print(w.wind())  # {'speed': 4.6, 'deg': 330}
print(w.humidity)  # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)  # {}
print(w.heat_index)  # None
print(w.clouds)  # 75

Weather = mgr.weather_at_place('London')  # give where you need to see the weather
w = Weather.weather

print(w.detailed_status)  # 'clouds'
print(w.wind())  # {'speed': 4.6, 'deg': 330}
print(w.humidity)  # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)  # {}
print(w.heat_index)  # None
print(w.clouds)  # 75
# http://api.openweathermap.org/data/2.5/weather?q=Goleta&APPID=bc406a21e03e694e8d239386b3b83d53
# python3 -m pip install --user requests
import requests, json
API_KEY = "YOUR KEY HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city_name = 'Goleta'
complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
response = requests.get(complete_url)
data = response.json()




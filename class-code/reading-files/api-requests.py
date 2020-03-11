# run the following in the terminal
# python -m pip install --user requests

import requests, json
API_KEY = YOUR_KEY_HERE
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city_name = 'Goleta'
complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
print(complete_url)
print("\n\n\n")
response = requests.get(complete_url)
data = response.json()
# print(data)
print(data["coord"])


astros_url = "http://api.open-notify.org/astros.json"

response = requests.get(astros_url).json()
print(f"There are currently {response['number']} astronauts on the ISS:")
for astro in response["people"]:
  print(f"\t{astro['name']}")



import requests
import json

my_API_Key = '55eff38189773bd48d8f34f3f5a87ec6' # never changing
zipcode_request = '10603' # should be read from .txt file passed to this script

# read zipcode from .txt file
# format OpenWeather API string with

# TEMPERATURE FROM API IS RETURNED IN KELVIN! NEEDS TO BE CONVERTED

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode_request},US&appid={my_API_Key}')
#response = JSON_to_Dict(response)

print(response.json())
print(response.json()['name']) # returns name of place
print(response.json()['main']) # returns temps(high/low/current), humidity
print(response.json()['weather'])
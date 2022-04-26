import requests
import json
import time


my_API_Key = '55eff38189773bd48d8f34f3f5a87ec6' # never changing
zipcode_request = '10603'

while True:
    time.sleep(1)
    txt_file = open('get-API-data-service.txt', 'r')
    zipcode_request = str(txt_file.read())  # reads zipcode from txt file
    txt_file.close()
    if zipcode_request != "":
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode_request},US&appid={my_API_Key}')
        zc_location_name = response.json()['name']
        zc_temp = response.json()['main']['temp']  # need to convert from Kelvin to Fahrenheit
        zc_condition = response.json()['weather'][0]['description']
        zc_icon = response.json()['weather'][0]['icon'] # returns icon ID
        to_be_written = str(zc_temp) + ", " + str(zc_condition) + ", " + str(zc_location_name) + ", " + str(zc_icon)
        txt_file = open('get-API-data-service.txt', 'w')
        txt_file.write(to_be_written)
        txt_file.close()
        time.sleep(5)


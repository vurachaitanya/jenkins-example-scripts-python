#print('Hello World')

import requests

# Hyderabad WOEID (Where On Earth ID) for MetaWeather
WOEID = 2295414

# API endpoint for weather data
URL = f'https://www.metaweather.com/api/location/{WOEID}/'

# Send a GET request to the API endpoint
response = requests.get(URL)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    temperature = data['consolidated_weather'][0]['the_temp']
    temperature_celsius = round(temperature, 2)
    print(f"The current temperature in Hyderabad is {temperature_celsius}°C.")
else:
    print("Failed to retrieve temperature data.")



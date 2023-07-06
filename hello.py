#print('Hello World')
import urllib.request
import json

# Hyderabad WOEID (Where On Earth ID) for MetaWeather
WOEID = 2295414

# API endpoint for weather data
URL = f'https://www.metaweather.com/api/location/{WOEID}/'

# Send a GET request to the API endpoint using urllib
response = urllib.request.urlopen(URL)

# Read the response and decode it
data = response.read().decode()

# Convert the response JSON string to a Python object
weather_data = json.loads(data)
temperature = weather_data['consolidated_weather'][0]['the_temp']
temperature_celsius = round(temperature, 2)
print(f"The current temperature in Hyderabad is {temperature_celsius}°C.")


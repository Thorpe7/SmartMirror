import os
import requests


# formats the weather output
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature: %s' % (name, desc, temp)
    except:
        final_str = 'City not found you dipass'

    return final_str

# gets the weather
def get_weather(city):
    weather_key = os.environ.get('WEATHER_API_KEY')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    return format_response(weather) # specifies that the result of this function will update label_weather's text
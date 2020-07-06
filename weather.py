import os
import requests
from dotenv import load_dotenv
load_dotenv()

# formats the weather output
def format_response(weather):
	degree_sign = u"\N{DEGREE SIGN}"
	try:
		desc = weather['weather'][0]['description'].capitalize()
		temp = round(weather['main']['temp'])
		hum = weather['main']['humidity']
		final_str = "%s \n%s" % (desc, temp) + str(degree_sign) + 'F'
		final_str = final_str + "\n%s" % (hum) + '%'
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

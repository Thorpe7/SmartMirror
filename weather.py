import os
import requests
from dotenv import Dotenv
dotenv = ("/home/pi/SmartMirror/.env")
import io
import base64
from urllib.request import urlopen

# formats the weather output
def format_response(weather):
	degree_sign = u"\N{DEGREE SIGN}"
	try:
		temp = round(weather['main']['temp'])
		hum = weather['main']['humidity']
		final_str = "%s" % (temp) + str(degree_sign) + 'F'
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

# gets weather conditions
def get_weather_conditions(city):
	weather_key = os.environ.get('WEATHER_API_KEY')
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	desc = weather['weather'][0]['description'].capitalize()
	return desc







########## Below functions handle fetching the icons from openweathermap url
def get_weather_icon(city):
	weather_key = os.environ.get('WEATHER_API_KEY')
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	weather_icon_url = 'http://openweathermap.org/img/wn/' + str(weather['weather'][0]['icon']) + '.png'
	return weather_icon_url # specifies that the result of this function will update label_weather's text

def get_icon():
	image_url = get_weather_icon("Minneapolis")
	response = requests.get(image_url)
	image_data = response.content
	#image_byt = urlopen(image_url).read()
	#print(image_byt)
	#image_b64 = base64.encodestring(image_byt)
	#photo = tk.PhotoImage(data=image_b64)
	#return photo
	return image_data



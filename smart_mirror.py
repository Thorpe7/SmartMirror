# time
import time

# Everything needed for tkinter
import datetime
import json
import os
import time
import tkinter.font
import traceback
from tkinter import *
import requests
import sys

# Grab environmental variables
from dotenv import load_dotenv
load_dotenv()




#specifying dimmensions for variable



# text sizes
x_large_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18
x_small_text_size = 14









# Beginning of tkinter 
root = Tk()
root.title('Smart Mirror')
root.configure(background='black') # creating the object and making it black

# Creating the dimessions of the screen
screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight()
root.geometry('{}x{}'.format(screen_width, screen_height)) # makes object the size of the screen 





# fonts for variables
font_time = tkinter.font.Font(family='Helvetica', size=x_large_text_size)
font_date = tkinter.font.Font(family='Helvetica', size=medium_text_size)
font_weather = tkinter.font.Font(family='Helvetica', size=small_text_size)
font_news = tkinter.font.Font(family='Helvetica', size=medium_text_size)

# formatting for date a time variables
time_format = '%I:%M'
date_format = '%A, %B %d, %Y'


#------------------------------------------------------------------------------------


# Frames for placing labels into
frame_top = Frame(root, background='black') # frame for top half of screen
frame_bottom = Frame(root, background='black') # frame for bottom half of screen

# TOP LEFT FRAME FOR DATE AND CLOCK
frame_t_left = Frame(frame_top, background='black') # top left frame


label_date = Label(frame_t_left, font=font_date,
                   bg='black',
                   fg='white')
label_clock = Label(frame_t_left, font=font_time,
                    bg='black',
                    fg='white')

# Layout of date and time
label_date.pack(side=TOP, anchor=W)
label_clock.pack(side=TOP, anchor=W)

# Clock function
def tick():
    s = time.strftime(time_format)
    d = time.strftime(date_format)
    if s != label_clock["text"]:
        label_clock["text"] = s
    if d != label_date["text"]:
        label_date["text"] = d
    label_clock.after(200, tick)


#--------------------------------------------------------------------------------------


# TOP RIGHT FRAME FOR WEATHER 
frame_t_right = Frame(frame_top, background='black')

label_weather = Label(frame_t_right, font=font_weather,
                   bg='black',
                   fg='white')

label_weather.pack(side=TOP, anchor=E)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature: %s' % (name, desc, temp)
    except:
        final_str = 'City not found you dipass'

    return final_str


def get_weather(city):
    weather_key = os.environ.get('WEATHER_API_KEY')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label_weather['text'] = format_response(weather) # specifies that the result of this function will update label_weather's text

# --------------------------------------------------------------------------------------

# BOTTOM RIGHT FRAME FOR NEWS HEADLINES

frame_b_right = Frame(frame_bottom, background='black') 
# frame_news = Frame(frame_b_right, background='black')
label_news = Label(frame_b_right, font=font_news,
                   bg='black',
                   fg='white')


def get_news():
	news_key = os.environ.get('NEWS_API_KEY')
	url = 'http://newsapi.org/v2/top-headlines?country=us'
	params = {'apikey': news_key, 'q': 'cnn'}
	response = requests.get(url, params = params)
	response_json = response.json()
	headlines = ''
	for i in response_json['articles']:
		headlines = headlines + i['title'] + '\n'
		# time.sleep(5)

	label_news['text'] = headlines


label_news.pack(side=RIGHT, anchor=SE)



	



#--------------------------------------------------------------------------------------


# Call functions that were created
tick()
get_weather('Minneapolis')
get_news()


#-------------------------------------------------------------------------------------
# Packing to display the objects that have been created





frame_t_left.pack(side=LEFT, anchor=N, padx=40, pady=40)
frame_t_right.pack(side=RIGHT, anchor=N, padx=40, pady=40)
frame_top.pack(expand=TRUE, fill=BOTH, side=TOP)

frame_b_right.pack(side=RIGHT, anchor=SE, padx=40, pady=40)
frame_bottom.pack(expand=TRUE, fill=BOTH, side=BOTTOM)


root.mainloop() # end of tkinter













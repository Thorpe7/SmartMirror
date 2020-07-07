# Function Files
import clock
import weather
import news
import mirror_calendar
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
from io import BytesIO
from PIL import ImageTk, Image

# Grab environmental variables
from dotenv import load_dotenv
load_dotenv()

# Specifying the local Display to be used
os.environ["DISPLAY"] = ':0'

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
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)



# fonts for variables
font_time = tkinter.font.Font(family='Helvetica', size=x_large_text_size)
font_date = tkinter.font.Font(family='Helvetica', size=medium_text_size)
font_conditions = tkinter.font.Font(family='Helvetica', size=medium_text_size)
font_news = tkinter.font.Font(family='Helvetica', size=medium_text_size)
font_calendar = tkinter.font.Font(family = 'Helvetica', size = medium_text_size)
font_weather = tkinter.font.Font(family = 'Helvetica', size = large_text_size)

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

label_clock['text'] = clock.tick()
label_date['text'] = clock.date()

def date_time_check():
  if clock.tick() != label_clock['text']:
    label_clock['text'] = clock.tick()
  if clock.date() != label_date['text']:
    label_date['text'] = clock.date()
  label_clock.after(200, date_time_check)
  label_date.after(3600000, date_time_check)

# Layout of date and time
label_clock.pack(side=TOP, anchor=W)
label_date.pack(side=TOP, anchor=W)

#--------------------------------------------------------------------------------------
# TOP RIGHT FRAME FOR WEATHER 

frame_t_right = Frame(frame_top, background='black')
label_weather = Label(frame_t_right, font=font_weather,
                   bg='black',
                   fg='white')
label_weather_conditions = Label(frame_t_right, font=font_conditions, bg = 'black', fg='white')
label_weather['text'] = weather.get_weather('Minneapolis')
label_weather_conditions['text'] = weather.get_weather_conditions('Minneapolis')
label_weather.pack(side=TOP, anchor=E)
label_weather_conditions.pack(side=TOP, anchor=W)
# Code commented out below is for adding icons from weather api, but they don't look good
#img = ImageTk.PhotoImage(Image.open(BytesIO(weather.get_icon())))
#label_weather_icon = Label(image=img)
#label_weather_icon.pack(side=TOP, anchor=W)

def weather_update():
  if weather.get_weather('Minneapolis') != label_weather['text']:
    label_weather['text'] = weather.get_weather('Minneapolis')
    label_weather.after(3600000, weather_update)


# --------------------------------------------------------------------------------------

# BOTTOM RIGHT FRAME FOR NEWS HEADLINES
frame_b_left = Frame(frame_bottom, background = 'black')
frame_b_right = Frame(frame_bottom, background='black')
label_news = Label(frame_b_left, font=font_news,
                   bg='black',
                   fg='white',
                   wraplength = 800)


# Creates function that iterates through list of headlines
label_news.pack(side = BOTTOM, anchor = SW)

def change_headlines():
	global headlines
	headlines = news.get_news_headlines()
	label_news.after(21600000, change_headlines)

change_headlines()
global n
n = 0
def get_headline():
	global headlines
	global n
	label_news['text'] = headlines[n]
	n+=1
	if n > len(headlines)-1:
		n = 0
	label_news.after(15000,get_headline)

#-------------------------------------------------------------------------------------

# BOTTOM LEFT FRAME FOR CALENDAR
label_calendar = Label(frame_b_left, font = font_calendar, bg = 'black', fg = 'white', wraplength = 800)
label_calendar.pack(side = TOP, anchor = W)
def calendar_text():
	label_calendar['text'] = str(mirror_calendar.dict_to_str(mirror_calendar.get_events()))
	label_calendar.after(21600000,calendar_text)

#--------------------------------------------------------------------------------------
# Call functions that were created
date_time_check()
weather_update()
get_headline()
calendar_text()

#-------------------------------------------------------------------------------------
# Packing to display the objects that have been created

frame_t_left.pack(side=LEFT, anchor=N, padx=40, pady=40)
frame_t_right.pack(side=RIGHT, anchor=NE, padx=40, pady=40)
frame_top.pack(expand=TRUE, fill=BOTH, side=TOP)
frame_b_left.pack(side = LEFT, anchor=SW,  padx = 40, pady = 40)
frame_b_right.pack(side = LEFT, anchor = SW, padx=40, pady=40)
frame_bottom.pack(expand=TRUE, fill=BOTH, side=BOTTOM)


root.mainloop()


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
font_weather = tkinter.font.Font(family='Helvetica', size=medium_text_size)
font_news = tkinter.font.Font(family='Helvetica', size=small_text_size)
font_calendar = tkinter.font.Font(family = 'Helvetica', size = medium_text_size)

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
label_date.pack(side=TOP, anchor=W)
label_clock.pack(side=TOP, anchor=W)


#--------------------------------------------------------------------------------------
# TOP RIGHT FRAME FOR WEATHER 

frame_t_right = Frame(frame_top, background='black')
label_weather = Label(frame_t_right, font=font_weather,
                   bg='black',
                   fg='white')

label_weather['text'] = weather.get_weather('Minneapolis')
label_weather.pack(side=TOP, anchor=E)


def weather_update():
  if weather.get_weather('Minneapolis') != label_weather['text']:
    label_weather['text'] = weather.get_weather('Minneapolis')
    label_weather.after(3600000, weather_update)


# --------------------------------------------------------------------------------------

# BOTTOM RIGHT FRAME FOR NEWS HEADLINES

frame_b_right = Frame(frame_bottom, background='black') 
# frame_news = Frame(frame_b_right, background='black')
label_news = Label(frame_b_right, font=font_news,
                   bg='black',
                   fg='white')

# Creates function that iterates through list of headlines
label_news.pack(side=RIGHT, anchor=SE)

global headlines
headlines =  news.get_news_headlines()

def get_headline():
  global headlines
  label_news['text'] = headlines[0]
  headlines.pop(0)
  if len(headlines) == 0:
    headlines = news.get_news_headlines()
  label_news.after(10000,get_headline)

#-------------------------------------------------------------------------------------

# BOTTOM LEFT FRAME FOR CALENDAR
frame_b_left = Frame(frame_bottom, background = 'black')
label_calendar = Label(frame_b_left, font = font_calendar, bg = 'black', fg = 'white')
label_calendar.pack(side = LEFT, anchor = SW)
label_calendar['text'] = str(mirror_calendar.get_events())




#--------------------------------------------------------------------------------------
# Call functions that were created
date_time_check()
weather_update()
get_headline()


#-------------------------------------------------------------------------------------
# Packing to display the objects that have been created

frame_t_left.pack(side=LEFT, anchor=N, padx=40, pady=40)
frame_t_right.pack(side=RIGHT, anchor=N, padx=40, pady=40)
frame_top.pack(expand=TRUE, fill=BOTH, side=TOP)
frame_b_left.pack(side = LEFT, anchor = SW, padx=40, pady=40)
frame_b_right.pack(side=RIGHT, anchor=SE, padx=40, pady=40)
frame_bottom.pack(expand=TRUE, fill=BOTH, side=BOTTOM)


root.mainloop()


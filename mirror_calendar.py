from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import datetime
import pickle
import time
import pandas

# What scopes the application will access
scopes = ['https://www.googleapis.com/auth/calendar.events.readonly']


### -------------------------------------------------------------------------------------------

# OAUTH SETUP
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes = scopes)
# user1_credentials = flow.run_local_server(port=0) #works for creating authorization object
# print(user1_credentials)
# pickle.dump(user1_credentials, open("user1_token.pkl", "wb")) # Dumps the authorization credentials object into pkl file

###-------------------------------------------------------------------------------------------

# Get your calendar
user1_credentials = pickle.load(open('user1_token.pkl', 'rb')) # Gets user credentials form pkl file
# print(user1_credentials)

service = build('calendar', 'v3', credentials = user1_credentials)
# print(service)

now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
result = service.events().list(calendarId='primary', timeMin=now,maxResults=10, singleEvents=True,orderBy='startTime').execute()

def dict_to_str(dict):
	if type(dict) == str:
		return dict
	if type(dict) != str:
		end_str = ""
		for key, value in dict.items():
			end_str = end_str + ' ' + str(key) + ': ' + str(value) + '\n'
		return end_str

def get_events():
	events = result.get('items', [])
	things = {}
	if not events:
		things = "No upcoming events found."
	for event in events:
		start = pandas.to_datetime(event['start'].get('dateTime'))
		if start == None:
			things.update({event['summary']: 'All Day Event'})
		else:
			start_datetime = str(start.strftime('%m/%d/%Y')) + ' ' + str(start.strftime('%H:%M'))
			things.update({event['summary']: start_datetime})
	#print(things)
	return things

dict = get_events()
dict_to_str(dict)

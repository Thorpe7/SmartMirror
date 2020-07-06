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
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes = scopes)
user1_credentials = flow.run_local_server(port=0) #works for creating authorization object
print(user1_credentials)
pickle.dump(user1_credentials, open("user1_token.pkl", "wb")) # Dumps the authorization credentials object into pkl file


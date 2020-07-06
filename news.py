import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()



# Creates a list of news headlines from news API
def get_news_headlines():
	news_key = os.environ.get('NEWS_API_KEY')
	url = 'http://newsapi.org/v2/top-headlines?country=us'
	params = {'apikey': news_key, 'q':'cnn'}
	response = requests.get(url, params = params)
	response_json = response.json() # Convert API output to python dict
	# print(response_json)
	global headlines
	headlines = []
	for i in response_json['articles']:
		headlines.append(i['title'])
	#print(headlines)

	return headlines


# Modify format of headlines
def format_headlines(headlines): 
	headlines = headlines
	for i in headlines:
		x = int(len(i)/2)

	# print(headlines)

get_news_headlines()
# format_headlines(headlines)

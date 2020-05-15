import os
import requests
import json




# Creates a list of news headlines from news API
def get_news_headlines():
	news_key = os.environ.get('NEWS_API_KEY')
	url = 'http://newsapi.org/v2/top-headlines?country=us'
	params = {'apikey': news_key, 'q': 'the-washington-post'}
	response = requests.get(url, params = params)
	response_json = response.json() # Convert API output to python dict
	global headlines
	headlines = []
	for i in response_json['articles']:
		headlines.append(i['title'])
	print(response.status_code)
	return headlines



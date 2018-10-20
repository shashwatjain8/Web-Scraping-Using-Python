# Scraping Cricket Scores from ESPN web page

import requests
from bs4 import BeautifulSoup
import pandas as pd

def getCricketScore():
	
	url = "http://static.cricinfo.com/rss/livescores.xml"

	score_data_raw = requests.get(url)
	score_data_soup = BeautifulSoup(score_data_raw.text, features = "html.parser")
	score_data = score_data_soup.find_all('description')
    
	for i, game in enumerate(score_data[1:], 1): 
		print game.text

getCricketScore()
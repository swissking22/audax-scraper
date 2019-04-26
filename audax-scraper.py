''' 
    Audax Scraper app that scrapes weather.com for today's weather forecast 
    in the city of Yaounde
'''

import requests
from bs4 import BeautifulSoup
import json

scrape_url = "https://weather.com/weather/today/l/CMXX0008:1:CM"

resp = requests.get(scrape_url)
soup = BeautifulSoup(resp.text, 'html.parser')

section_card = soup.find('div', {'class': 'today_nowcard-sidecar component panel'})

weather_prop_row = [ tr for tr in section_card.find_all('tr')]

weather_prop_row_header = []
weather_prop_row_values = []

for row in weather_prop_row: 
    # stores row header names in array
    weather_prop_row_header.append((row.th).text.strip())
    weather_prop_row_values.append((row.td.span).text.strip())

weather_set = dict(zip(weather_prop_row_header, weather_prop_row_values))

filename = 'weather_stats.json'

with open(filename, 'w') as fp:
    conv = json.dumps(weather_set, indent=4)
    print(conv, file=fp)

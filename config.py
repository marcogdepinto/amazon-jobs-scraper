"""
Use this file to save the configs for your script.
In the URL variable insert the URL you want to scrape
To get the last chromedrivers: https://sites.google.com/a/chromium.org/chromedriver/home
"""
import os

get_path = os.path.dirname(os.path.abspath(__file__))

# MacOs config
WEBDRIVER_PATH_MAC = '/usr/local/bin/chromedriver'

# Windows config
WEBDRIVER_PATH_WIN = get_path + '\\chromedrivers\\chromedriver.exe'

URL = 'https://www.amazon.jobs/en/search?base_query=manager&loc_query=Torino%' \
      '2C+Piedmont%2C+Italy&latitude=45.06236&longitude=7.67994&loc_group_id=&' \
      'invalid_location=false&country=ITA&city=Turin&region=Piedmont&county=Turin'

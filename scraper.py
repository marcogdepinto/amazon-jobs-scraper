"""
An application to scrape amazon.jobs website.
Passing an URL, it will return all the job IDs and job titles found in that URL.
Then, the app will create the job URL for each job found and, finally, will
save all the info in a CSV file.
"""
import re
import sys
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import URL
from config import WEBDRIVER_PATH_MAC
from config import WEBDRIVER_PATH_WIN


class Scraper:
    """
    This is the main class of the application
    """
    @staticmethod
    def create_browser(driver_path: str) -> webdriver.Chrome:
        """
        Creating a selenium object to simulate a browser.
        The headless tag creates an invisible browser.
        """
        browser_options = Options()
        browser_options.add_argument('--headless')
        browser_options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(executable_path=driver_path,
                                   options=browser_options)
        print('Done Creating Browser')
        return browser

    @staticmethod
    def get_job_and_location(soup: BeautifulSoup) -> list:
        """
        Getting job name, ID and location.
        Then, creating the URL of each job ID.
        """
        positions_list = []
        info_list = []

        for info in soup.findAll('div', {'class': 'info first col-12 col-md-8'}):
            positions_list.append(info)
        # print(positions_list)  # Debug

        for elem in positions_list:
            # Getting job title from the HTML
            regex = (r'job-title">([^<]+)')
            # Getting location from the HTML
            regex2 = (r'location-and-id">([^|]+)')
            # Getting job ID from the HTML
            regex3 = (r'Job ID: ([^<]+)')
            job_title = re.findall(regex, str(elem))
            location = re.findall(regex2, str(elem))
            job_id = re.findall(regex3, str(elem))
            # Creating a list of dictionaries with job_title, location, ID and url
            info_dict = {
                'job_title': job_title[0],
                'location': location[0],
                'job_id': job_id[0],
                'job_url': 'https://www.amazon.jobs/en/jobs/' + str(job_id[0])
            }
            # Appending every dictionary created to the list
            info_list.append(info_dict)

        # Creating the csv file
        Scraper.result_to_csv(info_list)

        # print(info_list)  # Debug
        return info_list

    @staticmethod
    def result_to_csv(lst: list) -> str:
        """
        Saving the output of the scraper into a CSV file.
        """
        keys = lst[0].keys()
        with open('example_output.csv', 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(lst)
        return 'Csv created!'

    @staticmethod
    def get_chrome_drivers() -> str:
        if sys.platform.startswith('linux'):
            driver_path = WEBDRIVER_PATH_MAC
        elif sys.platform.startswith('win'):
            driver_path = WEBDRIVER_PATH_WIN
        else:
            driver_path = "OS not supported."
        return driver_path


if __name__ == '__main__':
    print('Scraping started')
    BROWSER = Scraper.create_browser(driver_path=Scraper.get_chrome_drivers())
    BROWSER.get(url=URL)
    PAGE_HTML = BROWSER.page_source
    SOUP = BeautifulSoup(PAGE_HTML, features="html.parser")
    Scraper.get_job_and_location(SOUP)
    print('Your amazon.jobs url has been scraped. Check your output CSV file.')

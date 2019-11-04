# Amazon.jobs scraper

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Creating a CSV file of the jobs available at a particular URL of the Amazon.jobs website.

**Disclaimer**: this tool is not endorsed by Amazon in any way and I am not responsible of the usage you will make of it.

# Why I did this?
I wrote this software while I was searching for a job at Amazon. It can be used to pull all the information from a particular amazon.jobs URL and then elaborate them with Excel or other tools.

# How does this work?
Add to the config.py file [a research URL like this one](https://www.amazon.jobs/en/search?base_query=program+manager&loc_query=Torino%2C+Piedmont%2C+Italy&latitude=45.06236&longitude=7.67994&loc_group_id=&invalid_location=false&country=ITA&city=Turin&region=Piedmont&county=Turin). You can generate an url like this researching on amazon.jobs your target job and location. For example, this url has been generated researching for "Program Manager" in "Turin (IT)". 

Below an example of the structure of the output that you can get from this script:
```
job_title,location,job_id,job_url

Program Manager,"IT, Turin ",943396,https://www.amazon.jobs/en/jobs/943396
```

**Setup guide**

1) ```git clone https://github.com/marcogdepinto/amazon_jobs_scraper.git```;
2) ```$ pip install -r requirements.txt```;
3) Install Chrome Webdrivers [here](https://sites.google.com/a/chromium.org/chromedriver/home).

**How to run it**
- Open a command prompt and ```cd``` into the directory in which the file is saved;
- Edit the ```config.py``` inserting the path in which you have installed the chromedrivers on your machine and the url you want to scrape.
- type ```python scraper.py``` to run it.

**Developers stuff**

This code is [pylint](https://www.pylint.org/) and [mypy](http://mypy-lang.org/) 100% compliant.

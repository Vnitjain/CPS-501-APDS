# Author: Vinit Kirit Jain
# Assignment: Lab 13

# import the 'requests' library to make HTTP requests
import requests

# specify the URL of the web page to scrape
url = "https://realpython.github.io/fake-jobs/"

# send a GET request to the specified URL and store the response
response = requests.get(url)

# print the content of the response (HTML content of the web page)
print(response.text)

# import the 'BeautifulSoup' class from the 'bs4' library for web scraping
from bs4 import BeautifulSoup

# create a BeautifulSoup object and parse the HTML content using the 'html.parser'
bs_obj = BeautifulSoup(response.text, "html.parser")

# initialize an empty list to store the job titles
list_of_jobs = []

# iterate through all elements with the tag "h2" and class "title" in the BeautifulSoup object
for i in bs_obj.find_all("h2", "title"):

    # get the text content of each element and append it to the list_of_jobs
    list_of_jobs.append(i.get_text())

# print the list of job titles obtained from the web page
print(list_of_jobs)

# author: Vinit Kirit Jain
# date of creation: 2023-12-08


import requests  # importing the requests library
import re  # importing the regular expression library
from bs4 import BeautifulSoup  # importing the BeautifulSoup library from bs4
import matplotlib.pyplot as plt  # importing the pyplot module from matplotlib

link = "https://weather.com/weather/tenday/l/a05baa5a94807b678c0d9403cbc131381e2b33af1f6264959d7543eaa3b8ed7e"  # setting the url for the weather forecast

html_content = requests.get(
    link
)  # sending a get request to the url and storing the response

daylist = []  # initializing an empty list to store the days
templist = []  # initializing an empty list to store the temperatures

for weather_summary_content in BeautifulSoup(html_content.content).select(
    "[data-testid='DetailsSummary']"
):  # looping over each weather summary in the html content
    for day_content in BeautifulSoup(
        str(weather_summary_content), "html.parser"
    ).select(
        "[data-testid='daypartName']"
    ):  # looping over each day in the weather summary
        daylist.append(day_content.text)  # appending the text of the day to the daylist

    for temp_content in BeautifulSoup(
        str(weather_summary_content), "html.parser"
    ).select(
        "[data-testid='TemperatureValue']"
    ):  # looping over each temperature in the weather summary
        temperature = temp_content.text  # getting the text of the temperature
        temperature = re.sub(
            "\D", "", temperature
        )  # removing non-digit characters from the temperature
        if len(temperature) > 0:  # checking if the temperature is not empty
            templist.append(
                int(temperature)
            )  # appending the integer value of the temperature to the templist
figure, axis = plt.subplots()  # creating a figure and a set of subplots
axis.plot(
    daylist, templist[: len(daylist)]
)  # plotting the temperatures against the days

axis.set_xlabel("Date")  # setting the label for the x-axis
axis.set_ylabel("Temperature (F)")  # setting the label for the y-axis

plt.show()  # displaying the figure

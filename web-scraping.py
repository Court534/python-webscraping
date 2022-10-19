import requests
import pandas as pd

from bs4 import BeautifulSoup
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')

# seven-day searches for the first id seven-day-forecast
# forecast_items searches for the all the classes with the name tombstone-container 
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[1]
tomorrow = forecast_items[3]
friday = forecast_items[5]


# period if finding the first class with the name period-name and returning all the text within it using .get_text()
# short_desc if finding the first class with the name short-desc and returning all the text within it using .get_text()
# temp if finding the first class with the name temp and returning all the text within it using .get_text()
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

img = tonight.find("img")
desc = img['title']
print(desc)
print("\n")
period = tomorrow.find(class_="period-name").get_text()
short_desc = tomorrow.find(class_="short-desc").get_text()
temp = tomorrow.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

img = tomorrow.find("img")
desc = img['title']
print(desc)
print("\n")
period = friday.find(class_="period-name").get_text()
short_desc = friday.find(class_="short-desc").get_text()
temp = friday.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

img = friday.find("img")
desc = img['title']
print(desc)
print('\n')

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)
print('\n')

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
print(weather)
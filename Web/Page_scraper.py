#Followed tutorial on https://www.dataquest.io/blog/web-scraping-tutorial-python/

from bs4 import BeautifulSoup
import requests

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.77493000000004&lon=-122.41941999999995#.WsYQy3WWYso")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day_forecast = soup.find(id="seven-day-forecast")
forecast_items = seven_day_forecast.find_all(class_="tombstone-container")

if page.status_code == 200:
	for forecast in forecast_items:
		date = forecast.find(class_ = "period-name").get_text()
		short_desc = forecast.find(class_= "short-desc").get_text()
		temp = forecast.find(class_= "temp").get_text()

		print date
		print short_desc
		print temp + "\n"
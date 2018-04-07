from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.worldtimeserver.com/current_time_in_IN.aspx")
soup = BeautifulSoup(page.content, 'html.parser')

time = soup.find(id = "theTime")

if page.status_code == 200:
	print time.get_text()

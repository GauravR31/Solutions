#API Courtesy - "openweathermap.org, freegeoip.net"

import Fetch_weather_config
import json
import requests

def get_weather(city):
	weather_json = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}\
		&APPID={}&units=metric".format(city, Fetch_weather_config.key))

	weather_json = weather_json.json()

	print("City : {}\nTemperature : {} C\nMax : {} C\nMin : {} C\nHumidity : {}\nWind : {} km/h".format(
		weather_json["name"], weather_json["main"]["temp"], weather_json["main"]["temp_min"],
		weather_json["main"]["temp_max"], weather_json["main"]["humidity"], weather_json["wind"]["speed"]))

def main():
	while True:
		print("1. Weather for current location\n2. Weather for entered location\n3. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			location_url = 'http://freegeoip.net/json'
			loc = requests.get(location_url)
			loc = loc.json()
			city = loc["city"]
			get_weather(city)

		elif ch == 2:
			city = raw_input("Enter city to look up weather ")
			get_weather(city)
		
		elif ch == 3:
			break

		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()
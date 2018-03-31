from urllib2 import urlopen
from contextlib import closing
import json

ip = raw_input("Enter the IP address (press Enter for inserting own IP address) ")
# Automatically geolocate the connecting IP
url = 'http://freegeoip.net/json/{}'.format(ip)

with closing(urlopen(url)) as response:
    location = json.loads(response.read())
    location_city = location['city']
    location_state = location['region_name']
    location_country = location['country_name']

print("The IP is located in {}, {}, {}.".format(location_city, location_state, location_country))
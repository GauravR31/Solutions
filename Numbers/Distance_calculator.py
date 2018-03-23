import math,numpy
from math import sqrt
from pygeocoder import Geocoder

convertToRadians = (3.1415926536 / 180)

city1 = raw_input("Enter first city ")
city2 = raw_input("Enter second city ")

coord1 = Geocoder.geocode(city1)[0].coordinates
coord2 = Geocoder.geocode(city2)[0].coordinates

lat1 = coord1[0]
long1 = coord1[1]

lat2 = coord2[0]
long2 = coord2[1]

lat1 *= convertToRadians
long1 *= convertToRadians
lat2 *= convertToRadians
long2 *= convertToRadians

earth_rad = 6371

lat_sine = math.sin(((lat2 - lat1)/2))
long_sine = math.sin(((long2 - long1)/2))

x = sqrt((lat_sine ** 2) + (math.cos(lat1) * math.cos(lat2) * (long_sine ** 2)))

d = 2 * earth_rad * (numpy.arcsin(x))

while True:
	print("Choose a unit of distance\n1. Kilometres\n2. Miles\n3. Exit")
	ch = input("Enter your choice ")

	if ch==1:
		print("The distance between the two points is {} km".format(d))

	elif ch==2:
		print("The distance between the two points is {} miles".format(d*0.621371))

	elif ch==3:
		break

	else:
		print("Invalid choice")
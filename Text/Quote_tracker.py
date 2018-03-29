# API courtesy : https://www.alphavantage.co

from datetime import date, timedelta
import Quote_tracker_config
import urllib
import json

stock = raw_input("Enter the stock symbol ")

url = "https://www.alphavantage.co/query?"

mydict = {'function': 'TIME_SERIES_DAILY', 'symbol':stock, 'apikey':Quote_tracker_config.key}

query = urllib.urlencode(mydict)

res = urllib.urlopen(url + query).read()

jsonResponse = json.loads(res)

dailyQuote = jsonResponse["Time Series (Daily)"]

today = str(date.today())

if(today not in dailyQuote):
	today = str(date.today() - timedelta(1))
	todayQuote = dailyQuote[today] 

else:
	todayQuote = dailyQuote[today]

print("At closure of markets on {}, ".format(today))

if(todayQuote["1. open"] > todayQuote["4. close"]):
	print("{}'s stock has risen".format(stock))
elif(todayQuote["1. open"] < todayQuote["4. close"]):
	print("{}'s stock has fallen".format(stock))
else:
	print("No change")
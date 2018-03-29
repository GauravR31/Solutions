import feedparser
import pprint

rss = raw_input("Enter the link for RSS feed ")
feed = feedparser.parse(rss)

items = feed["items"]
args = ["title", "description"]

for item in items:
	print "#######################"

	for arg in args:
		if arg in item:
			print("{} : {}".format(arg,item[arg]))
import requests, time

def main():
	interval = input("Enter time interval in which to check the website (in minutes) ")
	url = raw_input("Enter URL ")

	if url.startswith('https://'):
		pass
	else:
		url = 'https://' + url

	while True:
		response = requests.get(url)

		if response.status_code > 400:
			print("{} is down at {}".format(url, time.ctime()))
		else:
			print("{} is up at {}".format(url, time.ctime()))

		time.sleep(interval*60)

if __name__ == '__main__':
	main()
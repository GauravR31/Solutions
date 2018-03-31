import whois

def main():
	IP = raw_input("Enter the domain name ")
	domain = whois.whois(IP)

	print(domain)

if __name__ == '__main__':
	main()
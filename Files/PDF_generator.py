import pdfkit

def main():
	while True:
		print("1. File to PDF\n2. URL to PDF\n3. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			file_name = raw_input("Enter the file name with path ")
			pdfkit.from_file(file_name, 'out.pdf')

		elif ch == 2:
			url = raw_input("Enter URL to convert to PDF ")
			pdfkit.from_url(url, 'out.pdf')

		elif ch == 3:
			break

		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()


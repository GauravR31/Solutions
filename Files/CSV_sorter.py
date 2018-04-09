import sys, csv, operator

data = csv.reader(open('Files.csv'), delimiter = ',')
sorted_list = sorted(data, key = lambda line: int(line[0]))

with open('New_files.csv', 'wb') as f:
	fileWriter = csv.writer(f, delimiter=',')
	for row in sorted_list:
		fileWriter.writerow(row)

	print("Sorted successfully")
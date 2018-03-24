n = input("Enter a number greater than 1 ")

i = 0

while n != 1:
	if (int(n)%2 == 0):
		n = int(n)/2
		i += 1

	else:
		n = (int(n)*3)+1
		i += 1

print("Number of steps required is {}".format(i))
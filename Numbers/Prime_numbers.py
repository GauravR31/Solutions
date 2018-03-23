from math import sqrt

def is_prime(g):
	if(g == 2):
		return True

	if(g % 2 == 0):
		return False

	for i in range(3, int(sqrt(g))+1, 2):
		if(g % i == 0):
			return False

	return True

choice = raw_input("Do you want a prime number(y/n)? ")

i = 2;

x = True
while(x):

	if choice == 'y':
		if (is_prime(i)):
			print(i)
			i += 1
			choice = raw_input("Do you want a prime number(y/n)? ")

		else:
			i += 1

	else:
		break


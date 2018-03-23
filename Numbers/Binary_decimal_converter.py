def d_to_b(dec):
	binary = ''
	while(dec > 0):
		binary += str(dec % 2)
		dec = dec / 2
	return binary[::-1]

def b_to_d(b):
	rev = str(b)[::-1]
	i = 0
	decimal = 0
	while(i < len(rev)):
		if(int(rev[i]) == 1):
			decimal += 2**i
		i+=1
	return decimal

def main():
	while True:
		print("1. Decimal to Binary\n2. Binary to Decimal\n3. Exit")
		c = input("Enter choice ")

		if c==1:
			n = input("Enter decimal ")
			print d_to_b(n)

		elif c==2:
			n = input("Enter binary ")
			print b_to_d(n)

		elif c==3:
			break

		else:
			print("Enter valid choice.")

if __name__ == '__main__':
	main()

		

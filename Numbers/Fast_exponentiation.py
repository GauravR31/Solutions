def expo(a, b):
	if(b == 1):
		return a

	if(b == 2):
		return a*a

	elif(b % 2 == 1):
		return a * expo(a, b-1)
	
	else:
		return expo(expo(a, b/2),2)

def main():
	a, b = raw_input("Enter the two numbers ").split()

	a = int(a)
	b = int(b)

	print expo(a,b)

if __name__ == '__main__':
	main()


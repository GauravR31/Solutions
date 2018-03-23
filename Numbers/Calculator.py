def main():
	while True:
		print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
		choice = input("Enter your choice ")

		if choice==1:
			a = input("Enter first number ")
			b = input("Enter second number ")
			print (a+b)

		elif choice==2:
			a = input("Enter first number ")
			b = input("Enter second number ")
			print (a-b)

		elif choice==3:
			a = input("Enter first number ")
			b = input("Enter second number ")
			print (a*b)

		elif choice==4:
			a = input("Enter first number ")
			b = input("Enter second number ")
			print (a/b)

		elif choice==5:
			break

		else:
			print("Enter valid choice.")

if __name__ == '__main__':
	main()
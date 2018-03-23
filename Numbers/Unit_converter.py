def temp():
	print("TEMPERATURE\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Exit")
	ch = input("Enter your choice ")

	if ch==1:
		c = input("Enter temperature in Celsius ")
		f = (c * 1.8) + 32
		return f

	elif ch==2:
		f = input("Enter temperature in Fahrenheit ")
		c = (f - 32) * 0.5556
		return c

	elif ch==3:
		return

	else:
		print("Enter valid choice.")

def mass():
	print("MASS\n1. Kg to lbs\n2. Lbs to kg\n3. Exit")
	ch = input("Enter your choice ")

	if ch==1:
		k = input("Enter mass in kg ")
		l = k * 2.20462
		return l

	elif ch==2:
		l = input("Enter mass in lbs ")
		k = l / 2.20462
		return k

	elif ch==3:
		return

	else:
		print("Enter valid choice.")

def volume():
	print("VOLUME\n1. L to m\u00b3\n2. m\u00b3 to L\n3. Exit")
	ch = input("Enter your choice ")

	if ch==1:
		lt = input("Enter volume in litres ")
		cm = lt * 0.001
		return cm

	elif ch==2:
		cm = input("Enter volume in m\u00b3 ")
		lt = cm / 0.001
		return lt

	elif ch==3:
		return

	else:
		print("Enter valid choice.")

def currency():
	print("CURRENCY\n1. Rupees to dollars\n2. Dollars to rupees\n3. Exit")
	ch = input("Enter your choice ")

	if ch==1:
		r = input("Enter amount in rupees ")
		d = r / 65.20
		return d

	elif ch==2:
		d = input("Enter amount in dollars ")
		r = d * 65.20
		return r

	elif ch==3:
		return

	else:
		print("Enter valid choice.")


def main():
	while True:
		print("1. Temperature\n2. Currency\n3. Mass\n4. Volume\n5. Exit")
		choice = input("Enter your choice ")

		if choice==1:
			print temp()

		elif choice==2:
			print currency()

		elif choice==3:
			print mass()

		elif choice==4:
			print volume()

		elif choice==5:
			break

		else:
			print("Enter valid choice")

if __name__ == '__main__':
	main()

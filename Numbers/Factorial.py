def fact_rec(n):
	if(n == 0 or n == 1):
		return 1
	
	else:
		return (n * fact_rec(n-1))

fact = 1

def fact_loop(n):
	for i in range(n, -1, -1):
		fact = fact * i

	return fact

def main():
	while True:
		print("1. Recursion\n2. Loop\n3. Exit")
		ch = input("Enter your choice ")

		if ch==1:
			num = input("Enter positive number ")
			print(fact_rec(num))

		elif ch==2:
			num = input("Enter positive number ")
			print(fact_rec(num))

		elif ch==3:
			break

		else:
			print("Enter valid choice")

if __name__ == '__main__':
	main()
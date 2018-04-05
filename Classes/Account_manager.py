class Account(object):
	"""docstring for Account"""
	def __init__(self, cust_id):
		self.cust_id = cust_id

class CheckingAccount(Account):
	"""docstring for CheckingAccount"""
	def __init__(self, cust_id, amount):
		self.cust_id = cust_id
		self.amount = amount

	def deposit(self, amt):
		self.amount += amt
		print("Current balance is {}".format(self.amount))

	def withdraw(self, amt):
		if amt > self.amount:
			print("Insufficient balance!")
		else:
			self.amount -= amt
			print("Current balance is {}".format(self.amount))

	def display_details(self):
		print("ID : {}\nBalance : {}".format(self.cust_id, self.amount))

class SavingsAccount(Account):
	"""docstring for SavingsAccount"""
	def __init__(self, cust_id, amount):
		self.cust_id = cust_id
		self.amount = amount

	def deposit(self, amt):
		self.amount += amt
		print("Current balance is {}".format(self.amount))

	def withdraw(self, amt):
		if amt > self.amount:
			print("Insufficient balance!")
		else:
			self.amount -= amt
			print("Current balance is {}".format(self.amount))

	def display_details(self):
		print("ID : {}\nBalance : {}".format(self.cust_id, self.amount))

class BusinessAccount(Account):
	"""docstring for BusinessAccount"""
	def __init__(self, cust_id, amount):
		self.cust_id = cust_id
		self.amount = amount

	def deposit(self, amt):
		self.amount += amt
		print("Current balance is {}".format(self.amount))

	def withdraw(self, amt):
		if amt > self.amount:
			print("Insufficient balance!")
		else:
			self.amount -= amt
			print("Current balance is {}".format(self.amount))

	def display_details(self):
		print("ID : {}\nBalance : {}".format(self.cust_id, self.amount))

def main():
	account_list = []
	John = CheckingAccount(26, 10000)
	Frank = SavingsAccount(8, 9000)
	Peter = BusinessAccount(1, 7000)
	Ashley = SavingsAccount(3, 6500)

	account_list = [John, Frank, Peter, Ashley]

	while True:
		print("1. Debit\n2. Credit\n3. Display account details\n4. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			flag = 0
			c_id = input("Enter your customer id ")
			for acc in account_list:
				if acc.cust_id == c_id:
					flag = 1
					amt = input("Enter withdrawl amount ")
					acc.withdraw(amt)
			
			if flag == 0:
				print("Incorrect customer id")

		elif ch == 2:
			flag = 0
			c_id = input("Enter your customer id ")
			for acc in account_list:
				if acc.cust_id == c_id:
					flag = 1
					amt = input("Enter deposit amount ")
					acc.deposit(amt)

			if flag == 0:
				print("Incorrect customer id")

		elif ch == 3:
			flag = 0
			c_id = input("Enter your customer id ")
			for acc in account_list:
				if acc.cust_id == c_id:
					flag = 1
					acc.display_details()

			if flag == 0:
				print("Incorrect customer id")

		elif ch == 4:
			break

		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()
		
		
		
		
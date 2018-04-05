class Product(object):
	"""docstring for Product"""
	def __init__(self, price, prod_id, quantity):
		self.price = price
		self.prod_id = prod_id
		self.quantity = quantity

	def increase_price(self):
		increase = input("Enter the amount by which to increase the cost ")
		self.price = self.price + increase

	def decrease_price(self):
		decrease = input("Enter the amount by which to decrease the cost ")
		self.price = self.price - decrease

	def increase_quantity(self):
		increase_quant = input("Enter the increase in quantity ")
		self.quantity = self.quantity + increase_quant

	def decrease_quantity(self):
		decrease_quant = input("Enter the decrease in quantity ")
		self.quantity = self.quantity - decrease_quant

	def display_quantity(self):
		print("Quantity of {} is {}".format(self.prod_id, self.quantity))

	def display_product(self):
		print("Product ID : {}\nQuantity : {}\nPrice : {}".format(self.prod_id, self.quantity, self.price))

class Inventory(object):
	"""docstring for Inventory"""
	def __init__(self):
		self.list = []

	def addProduct(self, product):
		self.list.append(product)

	def removeProduct(self, pId):
		i = 0

		for prod in self.list:
			if prod.prod_id == pId:
				self.list.remove(prod)
				i = 1
			else:
				pass

	def viewInventory(self):
		for prod in self.list:
			prod.display_product()
			print("\n")

def main():
	inventory = Inventory()

	while True:
		print "\n1. Add a product\n2. Update a product\n3. Remove a product\n4. View product\n5. View inventory\n6. Exit"
		ch = input("Enter your choice ")

		if ch == 1:
			quantity = input("Enter quantity of the product ")
			prod_id = raw_input("Enter ID of the product ")
			price = input("Enter the price of the product ")

			product = Product(price, prod_id, quantity)
			inventory.addProduct(product)

		elif ch == 2:
			print "1. Increase price\n2. Decrease price\n3. Increase quantity\n4. Decrease quantity"		
			c = input("Enter your choice ")

			if c == 1:
				prod_id = raw_input("Enter the product ID ")
				i = 0

				for prod in inventory.list:
					if prod.prod_id == prod_id:
						prod.increase_price()
						print("Price increased successfully!")
						i = 1
					else:
						pass

				if i == 0:
					print("Product not found.")

			elif c == 2:
				prod_id = raw_input("Enter the product ID ")
				i = 0

				for prod in inventory.list:
					if prod.prod_id == prod_id:
						prod.decrease_price()
						print("Price decreased successfully!")
						i = 1
					else:
						pass

				if i == 0:
					print("Product not found.")

			elif c == 3:
				prod_id = raw_input("Enter the product ID ")
				i = 0

				for prod in inventory.list:
					if prod.prod_id == prod_id:
						prod.increase_quantity()
						print("Quantity increased successfully!")
						i = 1
					else:
						pass

				if i == 0:
					print("Product not found.")

			elif c == 4:
				prod_id = raw_input("Enter the product ID ")
				i = 0

				for prod in inventory.list:
					if prod.prod_id == prod_id:
						prod.decrease_quantity()
						print("Quantity decreased successfully!")
						i = 1
					else:
						pass

				if i == 0:
					print("Product not found.")

			else:
				print("Invalid choice")
				break

		elif ch == 3:
			prod_id = raw_input("Enter the product ID ")
			i = 0

			for prod in inventory.list:
				if prod.prod_id == prod_id:
					inventory.removeProduct(prod_id)
					print("Product removed successfully!")
					i = 1
				else:
					pass

			if i == 0:
				print("Product not found.")

		elif ch == 4:
			prod_id = raw_input("Enter the product ID ")
			i = 0

			for prod in inventory.list:
				if prod.prod_id == prod_id:
					prod.display_product()
					i = 1
				else:
					pass

			if i == 0:
					print("Product not found.")

		elif ch == 5:
			inventory.viewInventory()

		elif ch == 6:
			break

		else:
			print("Invalid choice.")

if __name__ == '__main__':
	main()



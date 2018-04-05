class Flower(object):
	"""docstring for ClassName"""
	def __init__(self, f_type, rate, quantity):
		self.type = f_type
		self.rate = rate
		self.quantity = quantity

class Bouquet(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		self.flowers = []

	def add_flower(self):
		f_type = raw_input("Enter the flower type(Rose, Lily, Lotus, Daisy) ")
		
		if f_type == "Rose":
			f_quantity = input("Enter the flower quantity ")
			f = Flower(f_type, 10, f_quantity)
		
		elif f_type == "Lily":
			f_quantity = input("Enter the flower quantity ")
			f = Flower(f_type, 8, f_quantity)
		
		elif f_type == "Lotus":
			f_quantity = input("Enter the flower quantity ")
			f = Flower(f_type, 7, f_quantity)
		
		elif f_type == "Daisy":
			f_quantity = input("Enter the flower quantity ")
			f = Flower(f_type, 9, f_quantity)
		
		else:
			print("Invalid flower type")
			
		self.flowers.append(f)

	def update_flower(self):
		flag = 0

		f_type = raw_input("Enter the flower type to remove ")

		for i in range(0, len(self.flowers)):
			if self.flowers[i].type == f_type:
				f_quantity = input("Enter the new quantity(0 for none) ")
				flag = 1
				self.flowers[i].quantity = f_quantity

		if flag == 0:
			print("Flower not found")

	def bouquet_details(self):
		cost = 0

		for f in self.flowers:
			print("Type : {}\nRate : {}\nQuantity : {}\n".format(f.type, f.rate, f.quantity))
			cost += (f.rate * f.quantity)

		print("Total cost of the bouquet is {}".format(cost))

def main():
	b = Bouquet("Bouquet1")

	while True:
		print("1. Add flower\n2. Update or remove flower\n3. Bouquet details\n4. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			b.add_flower()

		elif ch == 2:
			b.update_flower()

		elif ch == 3:
			b.bouquet_details()

		elif ch == 4:
			break

		else:
			print("Invalid choice.")
		
if __name__ == '__main__':
	main()
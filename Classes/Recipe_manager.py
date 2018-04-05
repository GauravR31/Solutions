class Recipe(object):
	"""docstring for ClassName"""
	def __init__(self, r_name, ingredients, r_type):
		self.ingredients = ingredients
		self.r_name = r_name
		self.type = r_type

	def disp(self):
		print("Name : {}\nType : {}\nIngredients : {}".format(self.r_name, self.type, self.ingredients))

class Manager(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.recipe_list = []

	def add_recipe(self):
		r = Recipe("", "", "")
		r.r_name = raw_input("Enter the recipe's name ")
		r.type = raw_input("Enter the recipe's type (Starter, Main Course, Dessert) ")
		ing = raw_input("Enter the ingredients with space in between ")
		l = ing.split(" ")
		r.ingredients = l

		self.recipe_list.append(r)
		pass

	def display_recipes(self):
		for r in self.recipe_list:
			r.disp()

	def delete_recipe(self):
		name = raw_input("Enter the recipe name ")
		flag = 0
		for r in self.recipe_list:
			if r.r_name == name:
				self.recipe_list.remove(r)
				flag = 1

		if flag == 0:
			print("Recipe not found")

def main():
	recipe_manager = Manager()

	while True:
		print("1. Add a recipe\n2. Display recipes\n3. Delete recipes\n4. Exit")
		ch = input("Enter your choice ")

		if ch == 1:
			recipe_manager.add_recipe()
		elif ch == 2:
			recipe_manager.display_recipes()
		elif ch == 3:
			recipe_manager.delete_recipe()
		elif ch == 4:
			break
		else:
			print("Invalid choice")

if __name__ == '__main__':
	main()
		
		
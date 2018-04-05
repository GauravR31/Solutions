from math import sqrt, pi

class Shape(object):
	"""docstring for ClassName"""
	def area(self):
		pass

	def perimeter(self):
		pass

class Rectangle(Shape):
	"""docstring for Rectangle"""
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return (self.length * self.width)

	def perimeter(self):
		return (2 * (self.length + self.width))

class Triangle(Shape):
	"""docstring for Triangle"""
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def perimeter(self):
		return (self.side1 + self.side2 + self.side3)

	def area(self):
		s = perimeter(self)/2
		return sqrt((s * (s-self.side1) * (s-self.side2) * (s-self.side3)))

class Circle(Shape):
	"""docstring for ClassName"""
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return (pi * (self.radius ** 2))

	def perimeter(self):
		return (2 * pi * self.radius)

def main():
	while True:
		print "1. Circle\n2. Triangle\n3. Rectangle\n4. Exit"
		ch = input("Enter your choice ")

		if ch == 1:
			rad = input("Enter the radius of the circle ")
			circle = Circle(rad)
			print "1. Area\n2. Perimeter"
			c = input("Enter your choice ")

			if c == 1:
				print circle.area()
			elif c == 2:
				print circle.perimeter()

		elif ch == 2:
			side1 = input("Enter the first side of the triangle ")
			side2 = input("Enter the second side of the triangle ")
			side3 = input("Enter the third side of the triangle ")
			triangle = Triangle(side1, side2, side3)
			print "1. Area\n2. Perimeter"
			c = input("Enter your choice ")

			if c == 1:
				print triangle.area()
			elif c == 2:
				print triangle.perimeter()

		elif ch == 3:
			length = input("Enter the length of the rectangle ")
			width = input("Enter the width of the rectangle ")
			rectangle = Rectangle(length, width)
			print "1. Area\n2. Perimeter"
			c = input("Enter your choice ")

			if c == 1:
				print rectangle.area()
			elif c == 2:
				print rectangle.perimeter()

		elif ch == 4:
			break

		else:
			print("Invalid choice!")

if __name__ == '__main__':
	main()
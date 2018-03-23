from __future__ import print_function
from math import sqrt

class number:
	def __init__(self,x,y):
		self.r = x
		self.im = y

	def show(self):
		print("The result is {}+{}i".format(self.r, self.im))

	def negation(self):
		self.r = self.r * (-1)
		self.im = self.im * (-1)
		return self

	def inversion(self):
		root = sqrt((self.r * self.r) + (self.im * self.im))
		self.r = (self.r/root)
		self.im = -(self.im/root)
		return self

class complex:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self):
		print("Addition: ", end='')
		return number(self.x.r + self.y.r, self.x.im + self.y.im).show()

	def multiply(self):
		print("Multiplication: ", end='')
		return number(((self.x.r*self.y.r) - (self.x.im*self.y.im)), (self.x.r*self.y.im) + (self.x.im*self.y.r)).show()

def main():
	n1 = number(3,2)
	n2 = number(1,1)
	c = complex(n1, n2)

	print("The original complex numbers are {}+{}i and {}+{}i".format(n1.r, n1.im, n2.r, n2.im))

	c.add()
	c.multiply()

	print("Negation: ", end='')
	n2.negation().show()
	print("Inversion: ", end='')
	n2.inversion().show()	
	
if __name__ == '__main__':
		main()	
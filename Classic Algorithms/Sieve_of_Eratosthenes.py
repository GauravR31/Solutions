from math import sqrt

n = input("Enter upper limit of prime numbers you want ")

arr = [True] * n

arr[0] = False
arr[1] = False

for i in range(2, int(sqrt(n))):
	if arr[i] == True:
		for j in range(i**2, n, i):
			arr[j] = False

for i in range(len(arr)):
	if arr[i] == True:
		print i
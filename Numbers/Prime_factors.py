from math import sqrt

def is_prime(g):
	if(g == 2):
		return True

	if(g % 2 == 0):
		return False

	for i in range(3, int(sqrt(g))+1, 2):
		if(g % i == 0):
			return False

	return True

n = input("Enter a number ")

i = 2;

l = []

while(i < n):
	if(n%i == 0):
		l.append(i)
	i = i + 1

print(l)

for j in range(0, len(l)):
	if(is_prime(l[j])):
		print(l[j])

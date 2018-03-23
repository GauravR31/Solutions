import random

random.seed()

n = input("Enter number of coins to flip ")

h,t = 0, 0

while n > 0:
	d = random.choice([0,1])
	if d==0:
		t += 1
	else:
		h += 1
	n -= 1

print("No of heads: {}".format(h))
print("No of tails: {}".format(t))


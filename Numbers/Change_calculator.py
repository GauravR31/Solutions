cost = input("Enter the cost ")
money = input("Enter the money given ")

two_thousand, five_hundred, two_hundred, hundred, fifty, twenty, ten, five, two, change, tot_change = 0,0,0,0,0,0,0,0,0,0,0

if(money < cost):
	print("Please pay complete amount.")

else:
	change = money - cost
	tot_change = change
	if(change > 2000):
		two_thousand = change / 2000
		change = change % 2000

	if(change > 500):
		five_hundred = change / 500
		change = change % 500

	if(change > 200):
		two_hundred = change / 200
		change = change % 200

	if(change > 100):
		hundred = change / 100
		change = change % 100

	if(change > 50):
		fifty = change / 50
		change = change % 50

	if(change > 20):
		twenty = change / 20
		change = change % 20

	if(change > 10):
		ten = change / 10
		change = change % 10

	if(change > 5):
		five = change / 5
		change = change % 5

	if(change > 2):
		two = change / 2
		change = change % 2

print("Your change is {}.\n{} 2000's,\n{} 500's,\n{} 200's,\n{} 100's,\n{} 50's,\n{} 20's,\n{} 10's,\n{} 5's,\n{} 2's,\n{} 1's.".format(tot_change, two_thousand, five_hundred, two_hundred, hundred, fifty, twenty, ten, five, two, change))
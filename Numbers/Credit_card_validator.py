credit_card_no = input("Enter the credit card no ")

digits = [int(d) for d in str(credit_card_no)]

length = len(digits)

ul_digits = []

for i in range(length-2, -1, -2):
	ul_digits.append(digits[i]*2)

s1 = 0

for j in range(0, len(ul_digits)):
	s1 += (ul_digits[j]/10 + ul_digits[j]%10)

for k in range(length-1, -1, -2):
	s1 += digits[k]

if(s1 % 10 == 0):
	if(digits[0] == 3 and (digits[1] == 4 or digits[1] == 7)):
		print("American Express")

	elif digits[0] == 4:
		print("Visa")

	elif digits[0] == 5 and(digits[1] == 1 or digits[1] == 2 or digits[1] == 3 or digits[1] == 4 or digits[1] == 5):
		print("MasterCard")

else:
	print("Invalid card number")


	

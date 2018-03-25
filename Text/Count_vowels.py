vowels = ['a', 'e', 'i', 'o', 'u']

s = raw_input("Enter a string ")

a_count, e_count, i_count, o_count, u_count= 0, 0, 0, 0, 0

for i in s:
	if i in vowels[0]:
		a_count += 1

	elif i in vowels[1]:
		e_count += 1

	elif i in vowels[2]:
		i_count += 1

	elif i == vowels[3]:
		o_count += 1

	elif i == vowels[4]:
		u_count += 1

count = a_count + e_count + i_count + o_count + u_count

print("A : {}\nE : {}\nI : {}\nO : {}\nU : {}\nTotal : {}".format(a_count, e_count, i_count, o_count, u_count, count))
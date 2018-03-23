#referred a solution at https://github.com/checkcheckzz/coding-questions/blob/master/problem/Namenumbers.cpp

units = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ']
teens = ['ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']
tens = ['', 'ten ', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']
more = ['', 'thousand ', 'million ', 'billion ', 'trillion ', 'quadrillion ']

def underThousand(num1):
	name = ''

	if(num1 >= 100):
		name += units[num1/100] + ' hundred '
		num1 = num1 % 100
	
	if(num1 > 19):
		name += tens[num1/10]
		num1 = num1 % 10

	elif num1 >= 10 and num1 < 20:
		name += teens[num1]

	if num1 < 10:
		name += units[num1]

	return name

def translateNumber(num1):
	name = ''
	index = 0

	while num1>0:
		if(num1 % 1000 != 0):
			name = underThousand(num1%1000) + more[index] + name

		num1 /= 1000
		index += 1

	return name

def main():
	num = input("Enter number ")
	print translateNumber(num)

if __name__ == '__main__':
	main()
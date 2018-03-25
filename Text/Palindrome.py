s = ''
s = raw_input("Enter a string ")

if s == s[::-1]:
	print("{} is a palindrome".format(s))
else:
	print("{} is not a palindrome".format(s))
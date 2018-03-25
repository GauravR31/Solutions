vowels = ['a', 'e', 'i', 'o', 'u']

s = ''
s = raw_input("Enter a string ")

if s[0] in vowels:
	s = s + 'way'
else:
	s = s[1:] + s[0] + 'ay'

print s
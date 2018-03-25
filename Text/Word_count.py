f = open('words.txt', 'r')

ls = []
for word in f.read().split():
	ls.append(word)

print("{} words in words.txt".format(len(ls)))
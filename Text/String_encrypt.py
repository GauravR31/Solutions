def caesar(plaintext):
	key = input("Enter the key ")
	ciphertext = ''
	for character in plaintext:
		if character.isupper():
			character = ((ord(character) + key - 65) % 26) + 65

		elif character.islower():
			character = ((ord(character) + key - 97) % 26) + 97

		else:
			character = ord(character)

		character = chr(character)
		ciphertext += character

	print(ciphertext)

def caesar_decrypt(ciphertext):
	key = input("Enter the key to decrypt ")
	plaintext = ''
	for character in ciphertext:
		if character.isupper():
			character = ((ord(character) - key + 65) % 26) + 65

		elif character.islower():
			character = ((ord(character) - key - 97) % 26) + 97

		else:
			character = ord(character)

		character = chr(character)
		plaintext += character

	print(plaintext)

def vigenere(plaintext):
	key = raw_input("Enter the key ")

	plaintext = list(plaintext)
	ciphertext = []
	key = key.lower()
	key = list(key)
	j = 0

	for i in range(0, len(plaintext)):
		if j > len(key)-1:
			j = 0

		character = 0

		if plaintext[i].isupper():
			character = (((ord(plaintext[i]) - 65) + (ord(key[j]) - 97)) % 26) + 65
			j += 1

		elif plaintext[i].islower():
			character = (((ord(plaintext[i]) - 97) + (ord(key[j]) - 97)) % 26) + 97
			j += 1

		else:
			character = ord(plaintext[i])

		ciphertext.append(chr(character))
		
	print "".join(ciphertext)

def vigenere_decrypt(ciphertext):
	key = raw_input("Enter the key to decrypt ")
	ciphertext = list(ciphertext)
	plaintext = []
	key = key.lower()
	key = list(key)
	j = 0

	for i in range(0, len(ciphertext)):
		if j > len(key)-1:
			j = 0

		char = 0

		if ciphertext[i].isupper():
			char = (((ord(ciphertext[i]) + 65) - (ord(key[j]) - 97)) % 26) + 65
			j+=1

		elif ciphertext[i].islower():
			char = (((ord(ciphertext[i]) - 97) - (ord(key[j]) - 97)) % 26) + 97
			j += 1

		else:
			char = ord(ciphertext[i])

		plaintext.append(chr(char))

	print "".join(plaintext)

def main():
	print("1. Encrypt\n2. Decrypt\n3. Exit")
	c = input("Enter your choice ")

	while True:
		if c == 1:
			plaintext = raw_input("Enter text to encrypt ")

			print("Select encryption method\n1. Caesar\n2. Vigenere\n3. Exit")

			ch = input("Enter your choice ")
			if ch == 1:
				caesar(plaintext)
				break

			elif ch == 2:
				vigenere(plaintext)
				break
				
			elif ch == 3:
				break
			else:
				print "Invalid choice."

		elif c == 2:
			ciphertext = raw_input("Enter text to decrypt ")

			print("Select decryption method\n1. Caesar\n2. Vigenere\n3. Exit")

			ch = input("Enter your choice ")
			if ch == 1:
				caesar_decrypt(ciphertext)
				break
				
			elif ch == 2:
				vigenere_decrypt(ciphertext)
				break

			elif ch == 3:
				break
			
			else:
				print "Invalid choice."

		elif c == 3:
			break

		else:
			print "Invalid choice."
			break

if __name__ == '__main__':
	main()

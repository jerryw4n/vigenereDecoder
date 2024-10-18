def decrypt_vigenere(ciphertext, key):
	# Create array for deciphered message
	decrypted_text = []
	# Create variable to match key length for when to loop back to beginning of the key
	key_length = len(key)

	# Decrypt each letter
	for i, letter in enumerate(ciphertext):
		letter_pos = ord(letter) - ord('a')
		key_pos = ord(key[i % key_length]) - ord('a')
		decrypted_letter = (letter_pos - key_pos) % 26 + ord('a')
		decrypted_text.append(chr(decrypted_letter))

	return ''.join(decrypted_text)

# Get user input for ciphertext and key
ciphertext = input("Enter the ciphertext: \n")
print("")
key = input("Enter the key: \n")
print("")

# Decrypt the ciphertext using the Vigenere cipher function
decrypted_message = decrypt_vigenere(ciphertext, key)
print("Decrypted message: ")
print(decrypted_message)
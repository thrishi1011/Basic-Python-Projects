# Encryption Program
import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + ' '
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

plain_text = input("Enter your message: ")
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Your original message: {plain_text}")
print(f'Your encrypted message: {cipher_text}')

cipher_text = input('Enter your encrypted message: ')
plain_text = ''

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f'Your encrypted message: {cipher_text}')
print(f'Your original message: {plain_text}')


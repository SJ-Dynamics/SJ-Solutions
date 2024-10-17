import string
import random

char_set = string.ascii_letters + string.digits + string.punctuation

def generate_sbox(key):
    seed = sum(ord(char) for char in key)
    shuffled_chars = list(char_set)
    random.Random(seed).shuffle(shuffled_chars)
    s_box = {char_set[i]: shuffled_chars[i] for i in range(len(char_set))}
    inverse_s_box = {shuffled_chars[i]: char_set[i] for i in range(len(char_set))}
    return s_box, inverse_s_box

def encrypt(message, s_box):
    encrypted_message = ''.join(s_box.get(char, char) for char in message)
    return encrypted_message

def decrypt(encrypted_message, inverse_s_box):
    decrypted_message = ''.join(inverse_s_box.get(char, char) for char in encrypted_message)
    return decrypted_message

key = input("Enter a 32-character key: ")

if len(key) != 32:
    raise ValueError("Key must be 32 characters long.")

s_box, inverse_s_box = generate_sbox(key)

choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

if choice == 'e':
    message = input("Enter a message to encrypt: ")
    encrypted_message = encrypt(message, s_box)
    print("Encrypted Message:", encrypted_message)
elif choice == 'd':
    encrypted_message = input("Enter a message to decrypt: ")
    decrypted_message = decrypt(encrypted_message, inverse_s_box)
    print("Decrypted Message:", decrypted_message)
else:
    print("Invalid choice. Please select 'e' for encryption or 'd' for decryption.")

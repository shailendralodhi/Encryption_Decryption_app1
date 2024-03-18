import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# Encryption

message = input("Enter your message here : ")
cipher_text=""

for letter in message:
    index = chars.index(letter)
    cipher_text+=key[index]

    
print(f"Encrypted message: {cipher_text}")


#Decryption

cipher_text = input("Enter your message here : ")
cryptedmessage=""

for letter in cipher_text:
    index=key.index(letter)
    cryptedmessage+=chars[index]

print(f"encrypted message :{cipher_text}")

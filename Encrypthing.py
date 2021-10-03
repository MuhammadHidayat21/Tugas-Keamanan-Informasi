from cryptography.fernet import Fernet

file = open('key.txt', 'rb')			
key = file.read()
file.close()

with open('text.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open('textsecured.txt', 'wb') as f:
    f.write(encrypted)


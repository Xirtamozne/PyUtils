from cryptography.fernet import Fernet

def writeKey(keyfile):
    writeKey = Fernet.generate_key()
    file = open(keyfile, 'wb')
    file.write(writeKey)
    file.close()

def readKey(keyfile):
    file = open(keyfile, 'rb')
    readKey = file.read()
    file.close()
    key = Fernet(readKey)
    return key

def encryptMessage(key, message):
    return key.encrypt(message.encode())

def decryptMessage(key, message):
    return key.decrypt(message)

def encryptFile(decryptedFile, encryptedFile, key):

    with open(decrypted_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encryptedFile, 'wb') as f:
        f.write(encrypted)

def decryptFile(decryptedFile, encryptedFile, key):
    with open(encrypted_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(decryptedFile, 'wb') as f:
        f.write(decrypted)

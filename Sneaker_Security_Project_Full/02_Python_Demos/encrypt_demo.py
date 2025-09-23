from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

if __name__ == "__main__":
    key = generate_key()
    print("Encryption Key (keep this secret!):", key.decode())

    message = input("Enter a message to encrypt: ")
    encrypted = encrypt_message(key, message)
    print("Encrypted:", encrypted.decode())

    decrypted = decrypt_message(key, encrypted)
    print("Decrypted:", decrypted)

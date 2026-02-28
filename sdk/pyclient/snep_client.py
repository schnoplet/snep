from cryptography.fernet import Fernet
import hashlib

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt_message(key, token):
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()

def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
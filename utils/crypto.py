from cryptography.fernet import Fernet
import hashlib

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key: bytes, message: str) -> bytes:
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(key: bytes, token: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token).decode()

def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()
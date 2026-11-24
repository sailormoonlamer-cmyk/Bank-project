

from cryptography.fernet import Fernet

KEY = b"PASTE_YOUR_KEY_HERE"

cipher = Fernet(KEY)

def encrypt(data: bytes) -> bytes:
    return cipher.encrypt(data)

def decrypt(data: bytes) -> bytes:
    return cipher.decrypt(data)
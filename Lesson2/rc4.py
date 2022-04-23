from Crypto.Cipher import ARC4
from Crypto.Hash import SHA


def rc4(plaintext, key):
    cipher = ARC4.new(key)
    return cipher.encrypt(plaintext)

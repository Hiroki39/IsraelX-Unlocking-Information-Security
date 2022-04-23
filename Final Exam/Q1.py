import random
import hashlib
import os
from Crypto.Cipher import AES
from Crypto import Random

# you can use the imports, and you can solve with your own imports

p = 283
g = 47


class SecureChannel:

    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.a = random.randint(1, 20)

    def publish(self):
        return self.g**self.a % self.p

    def encrypt(self, gb, text):
        secret = gb**self.a % self.p
        m = hashlib.sha256()
        m.update(str(secret).encode())
        key = m.digest()[:16]
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(text.encode())

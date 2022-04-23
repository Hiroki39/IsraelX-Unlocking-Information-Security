from Crypto.Cipher import AES
from Crypto import Random


def aes_encrypt(plaintext, key):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(plaintext)
    return ciphertext


def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext[AES.block_size:]).decode('latin1')

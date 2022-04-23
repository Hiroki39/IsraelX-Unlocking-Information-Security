import itertools
from Crypto import Random
from Crypto.Cipher import AES
from aes_cbc import aes_decrypt
from is_english import is_english


def brute_force_aes(ciphertext):
    iv = ciphertext[:AES.block_size]
    encrypted_text = ciphertext[AES.block_size:]
    for i in range(1000000):
        key = ('036' + f'{i:06}' + '0000000').encode('latin1')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(
            encrypted_text).decode('latin1')
        if is_english(plaintext):
            return plaintext, key

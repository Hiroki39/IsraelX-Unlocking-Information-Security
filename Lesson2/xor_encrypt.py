def encrypt(plaintext, k):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(k[i]))
    return ciphertext

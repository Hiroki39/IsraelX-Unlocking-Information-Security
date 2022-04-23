def encrypt(plaintext, k):
    ciphertext = ""
    for c in plaintext:
        if ord(c) + k > 122:
            ciphertext += chr(ord(c) + k - 26)
        else:
            ciphertext += chr(ord(c) + k)
    return ciphertext

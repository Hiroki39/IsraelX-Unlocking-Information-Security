def get_prg(plaintext_size, k):
    i, j = 0, 0
    k = list(k)
    keystream = ""
    for n in range(plaintext_size):
        i = (i + 1) % len(k)
        j = (j + ord(k[i])) % len(k)
        k[i], k[j] = k[j], k[i]
        keystream += k[(ord(k[i]) + ord(k[j])) % len(k)]
    return keystream


def fake_rc4(plaintext, keystream):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(keystream[i]))
    return ciphertext

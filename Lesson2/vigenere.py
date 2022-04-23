def vigenere_encrypt(plaintext, codeword):
    ciphertext = ""
    for i in range(len(plaintext)):
        ord_of_char = ord(codeword[i % len(codeword)]) - \
            ord(plaintext[0]) + ord(plaintext[i])
        if ord_of_char < 65:
            ord_of_char += 26
        if ord_of_char > 90:
            ord_of_char -= 26
        ciphertext += chr(ord_of_char)
    return ciphertext

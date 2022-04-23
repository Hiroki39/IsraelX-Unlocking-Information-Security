n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)


def encrypt(m, public_key):
    return m**e % n


def decrypt(c, private_key):
    return c**d % n

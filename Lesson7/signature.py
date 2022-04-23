n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)


def sign(m, private_key):
    return m**d % n


def verify(m, s, public_key):
    return m == (s**e % n)

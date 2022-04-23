from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')


def encrypt(m, public_key):
    rsa_public_key = RSA.importKey(public_key)
    return pow(m, rsa_public_key.e, rsa_public_key.n)


def decrypt(c, private_key):
    rsa_private_key = RSA.importKey(private_key)
    return pow(c, rsa_private_key.d, rsa_private_key.p)

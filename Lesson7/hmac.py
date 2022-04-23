from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'


def weak_hmac(m, k, ipad, opad):
    s_ipad = bytes([a ^ b for a, b in zip(k, ipad)])
    s_opad = bytes([a ^ b for a, b in zip(k, opad)])
    h = sha1()
    h.update(s_opad)
    h2 = sha1()
    h2.update(s_ipad)
    h2.update(m)
    h.update(h2.digest())
    return h.hexdigest()

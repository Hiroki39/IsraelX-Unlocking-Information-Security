import hashlib
import itertools


def weak_md5(s):
    return hashlib.md5(s.encode()).digest()[:5]


def find_collisions():
    i = 1
    hashed = {}
    while True:
        for tup in itertools.product((chr(i) for i in range(97, 123)), repeat=i):
            string = ''.join(tup)
            if weak_md5(string) in hashed:
                return string, hashed[weak_md5(string)]
            hashed[weak_md5(string)] = string
        i += 1

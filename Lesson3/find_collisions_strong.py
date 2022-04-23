import hashlib
import itertools


def md5(s):
    return hashlib.md5(s.encode()).digest()


def find_collisions():
    i = 1
    hashed = {}
    while True:
        for tup in itertools.product((chr(i) for i in range(97, 123)), repeat=i):
            string = ''.join(tup)
            if md5(string) in hashed:
                return string, hashed[md5(string)]
            hashed[md5(string)] = string
        i += 1

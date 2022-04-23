import itertools


def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r


def crack(s):
    i = 1
    hashed = simple_hash(s)
    while True:
        for tup in itertools.product((chr(i) for i in range(97, 123)), repeat=i):
            string = ''.join(tup)
            if string == s:
                continue
            if simple_hash(string) == hashed:
                return string
        i += 1

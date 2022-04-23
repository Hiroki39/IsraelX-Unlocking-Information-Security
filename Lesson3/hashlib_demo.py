import hashlib

string = "Hello, world!".encode()
print(hashlib.md5(string).hexdigest())
print(hashlib.sha1(string).hexdigest())
print(hashlib.sha256(string).hexdigest())

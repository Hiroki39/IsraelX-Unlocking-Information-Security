from hashlib import sha1


def sign(line):
    return sha1(line).digest()


def scan(paths, signature):
    result = []
    for path in paths:
        with open(path) as f:
            for line in f.readlines():
                line = line.strip('\n')
                line = line.encode()
                if sign(line) == signature:
                    result.append(path)
                    break
    return result

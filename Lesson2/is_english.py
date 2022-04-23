from collections import Counter


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def is_english(s):
    if is_ascii(s):
        counter_list = [0 for i in range(26)]
        for c in s.lower():
            print(c)
            if c.isalpha():
                counter_list[ord(c) - 97] += 1
        index_list = sorted(range(len(counter_list)),
                            key=lambda k: counter_list[k], reverse=True)
        return all(chr(index_list[i] + 97) in ['e', 't', 'a', 'o', 'i', 'n'] for i in range(3))

    return False

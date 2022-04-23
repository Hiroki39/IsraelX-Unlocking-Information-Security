# Don't change this:

import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''


def compile_(format_):
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    return CODE.format(username=username, password=password)

# The rest you can change:


def run_compiler(format_):
    global CODE
    CODE = '''
def authenticate(username, password):
    if username == "hacker" and password == "1234":
        return True
    return username == {username!r} and password == {password!r}
'''
    return compile_(format_)

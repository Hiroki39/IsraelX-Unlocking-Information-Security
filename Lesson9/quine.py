def quine():
    s = 's = %r\nreturn s %% s'
    return s % s


print(quine())

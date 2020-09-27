# EASY : CamelCase

def camelcase(s):
    ls = list(s)
    c = 0
    for i in range(len(ls)):
        if ls[i].isupper():
            c += 1
            continue
    return (c+1)
# EASY : Super reduced Strings

def superReducedString(s):
    ls = list(s)
    i = 0
    while(i < len(ls)-1):
        if ls[i] == ls[i+1]:
            del ls[i]
            del ls[i]
            i=0
            if len(ls) == 0:
                return ('Empty String')
                break
        else:
            i += 1
    return(''.join(ls))
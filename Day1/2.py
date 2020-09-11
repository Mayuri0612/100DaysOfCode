#MEDIUM : The power sum

def powerSum(X, N, cnum = 1):
    p = pow(cnum, N)
    if p > X:
        return 0
    elif p == X:
        return 1
    else:
        return powerSum(X, N, cnum + 1) + powerSum(X - p, N, cnum+1)
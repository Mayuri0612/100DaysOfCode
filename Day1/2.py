#MEDIUM : The power sum

def powerSum(x, N, cnum = 1):
    p = pow(cnum, N)
    if p > x:
        return 0
    elif p == x:
        return 1
    else:
        return powerSum(x, N, cnum + 1) + powerSum(x - p, N, cnum+1)

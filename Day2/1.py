#MEDIUM : Recursive digit sum

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
'''
def superDigit(n, k):
    p = k * int(n)
    def sumOfDigit(p):
        add = 0
        if p < 10:
            return p
        else:
            while p > 0:
                temp = p % 10
                add += temp
                p = p // 10
        return sumOfDigit(add)
    res = sumOfDigit(p)
    return res

'''
def superDigit(n, k):
    digits = map(int, list(n))
    return sumOfDigit(k * str(sum(digits)))

def sumOfDigit(p):
    if len(p) == 1:
        return int(p)
    else:
        d = map(int, list(p))
        return sumOfDigit(str(sum(d)))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

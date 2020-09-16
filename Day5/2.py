#EASY : Min-max sum

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def minMaxSum(arr):
    x = sum(arr)
    mini = x-(max(arr))
    maxi = x-(min(arr))
    print(mini, end = ' ')
    print(maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    minMaxSum(arr)

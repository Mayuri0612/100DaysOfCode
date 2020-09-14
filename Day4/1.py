# EASY : A+B

from sys import stdin
sums = []
for i in stdin:
    data = list(map(int, i.split()))
    sums.append(sum(data))
for i in sums:
    print(i, sep="\n")
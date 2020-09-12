#HARD : K-factorizaion
def kFactorization(n, arr, cur, result):
    if cur == n:
        allres.append(list(result))
        return True
    elif cur > n:
        return False

    for ind, val in enumerate(arr):
        result.append(cur * val)
        kFactorization(n, arr[ind:], cur * val, result)
        result.pop()
    return False

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().strip().split(' '))))
    result = [1]
    allres = []
    kFactorization(n, arr, 1, result)

    if not allres:
        print(-1)
    else:
        print(' '.join(list(map(str, min(allres, key = len)))))

# MEDIUM : Password Cracker

import sys
sys.setrecursionlimit(20000)

def finalCheck(passwords, attempt):
    allpass = "".join(passwords)
    res = True
    for i in attempt:
        if i not in allpass:
            res = False
            break
    return res

def cracker(passwords, attempt, solution, dictt):
    if len(attempt) == 0:
        return True

    if attempt in dictt:
        return False
    
    for i in passwords:
        if attempt.startswith(i):
            solution.append(i)
            dictt[attempt] = True
            if cracker(passwords, attempt[len(i):], solution, dictt) == True:
                return True
            else:
                solution.pop()
    return False



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        passwords = input().strip().split(' ')
        attempt = input().strip()
        solution = [] #to capture all the valid words of attempt
        dictt = {}
        if finalCheck(passwords, attempt) and cracker(passwords, attempt,solution, dictt):
            print(" ".join(solution))
        else:
            print("WRONG PASSWORD")
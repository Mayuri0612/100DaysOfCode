#EASY : GCD String (partially accepted)
def g(a, b):
    if a%b==0:
        o = "1"
        o += '0'*(a-1)
        return o
    else:
        return (g(b, a%b)*(a//len(g(b, a%b))+1))[:a]
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(int(g(x, y), 2)%1000000007)
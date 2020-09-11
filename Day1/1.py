#EASY : fibonacci recursive
def fibonacci(n):

    # Write your code here.
    if n <= 1:
       return n
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        return res
    
    

n = int(input())
print(fibonacci(n))

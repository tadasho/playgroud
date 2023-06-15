from functools import cache

@cache
def fib(n):
    //print("fib("+str(n)+")", end=" ")
    if n<3: return 1
    return fib(n-2) + fib(n-1)

print(fib(100))
def fib(n):
    memo = {1:1, 2:1}
    def _fib(n):
        if n in memo : return memo[n]
        memo[n] = _fib(n-2) + _fib(n-1)
        return memo[n]
    return _fib(n)

print(fib(100))
# Recursão com memoização/memorização
def fatorial_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    
    memo[n] = n * fatorial_memo(n-1, memo)
    return memo[n]

'''CPU times: total: 0 ns
Wall time: 5.01 μs'''

print(fatorial_memo(10))

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))
'''%time fib(10)
CPU times: total: 0 ns
Wall time: 3.58 μs
Out[12]: 55'''

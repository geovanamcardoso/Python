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

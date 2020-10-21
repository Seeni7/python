def fib_default_memoized(n, cache={}):
    if n in cache:
        ans = cache[n]
    elif n<= 2:
        ans = 1
        cache[n] = ans
    else:
        ans = fib_default_memoized(n - 2) + fib_default_memoized(n - 1)
        cache[n] = ans

        print(ans)


def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return (fib(n-1) + fib(n-2))

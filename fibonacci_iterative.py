#iterative
def fib_iterative(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n>1):
        fn = 0
        fn1 = 1
        fn2 = 2

        for i in range(3, n):
            fn = fn1+fn2
            fn1 = fn2
            fn2 = fn
        return fn

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return (fib(n-1) + fib(n-2))


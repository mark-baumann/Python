#recursive
def fibonacciRecursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


def fibonacciIterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacciDynamic(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacciDynamic(n - 1, memo) + fibonacciDynamic(n - 2, memo)
    return memo[n]


print(fibonacciIterative(10))
print(fibonacciDynamic(10))
print(fibonacciRecursive(10))
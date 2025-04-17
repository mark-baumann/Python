def square(n):
    y = 1
    i = 0

    for i in range(0, n - 1):
        i += 1
        print(f"i= {i}")
        j = 0
        for j in range(0, n - 1):
            j += 1
            y += (i - j)
            print(f" j= {j}")
    return y

"""
n = 4
result = square(n)
print(f"Ergebnis: {result}")
"""

def linear(n):
    y = 1
    i = 0

    for i in range(0, n - 1):
        i += 1
        print(f"i= {i}")
        y *= 2

    return y


n = 5
result = linear(n)
print(f"Ergebnis: {result}")


def logalg(n):
    y = 1
    k = n

    while k > 1:
        print(f"k= {k}")
        k = k // 2
        y += 1
    return y - 1


n = 32
result = logalg(n)
print(f"Ergebnis: {result}")


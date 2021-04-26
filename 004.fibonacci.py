from functools import reduce

# FIBONACCI RECURSION


def fibo_rec(n):
    if n < 2:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

#fib = lambda x: fib(x-1) + fib(x + 1) if x > 2 else 1


print(fibo_rec(8))

# FIBONACCI LOOP самый быстрый
lister = []


def fibo(n):
    fib1 = 1
    fib2 = 1
    lister.extend((fib1, fib2))
    for x in range(3, n + 1):
        fib1, fib2 = fib2, fib1 + fib2
        lister.append(fib2)
    return fib2


print(fibo(3))
print(lister)

# ODER SO


def fib_loop(n):
    """fibonacci loop"""
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib_loop(10))

# FIBONACCE PRINT WHILE


def fibo(item):
    a = 0
    b = 1
    while a < item:
        print(a, end=" ")
        a, b = b, a + b


fibo(2000)


# FIBONACCE MEINE

def fibo(n, start=1):
    if n == 0:
        l = []
    else:
        # l = [0, 1] # если хотим начинать с 0
        l = [1]  # если хотим начинать с 1
        starter = start
        # for x in range(3, n + 1): # если хотим начинать с 0
        for x in range(2, n + 1):  # если хотим начинать с 1
            l.append(starter)
            starter = l[x - 1] + l[x - 2]
    return l


print(fibo(10))


# FIBONACCE MEINE2
start = (1, 0)


def fibo(fn):
    global start
    for x in range(1, 10):
        start = fn(start, (start[0] + start[1], start[0]))
    return start[0]


print(fibo(lambda x, y: y))


# FIBONACCE REDUCE

def fibo_reduce(n):
    start = (1, 0)
    dummy = range(n - 1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, start)
    return fib_n[0]


print(fibo_reduce(10))

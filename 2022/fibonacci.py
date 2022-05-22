# Fibonacci numbers using while
def printFibonacci(n):
    a = 0
    b = 1
    while a <= n:
        print(a)
        c = a+b
        a = b
        b = c

n = 20
printFibonacci(n)

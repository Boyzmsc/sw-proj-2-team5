import time

def iterfibo (n):
    num0 = 0
    num1 = 1
    num2 = 0
    if n == 0:
        ans = num0
    elif n == 1:
        ans = num1
    else:
        while n > 1:
            num2 = num0 + num1
            num0 = num1
            num1 = num2
            n = n - 1
        ans = num2
    return ans

def fibo (n):
    if n<= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
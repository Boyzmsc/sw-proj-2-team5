import time
import random

def Fibo(n):
    if n <= 1:
        return n
    return Fibo(n-1) + Fibo(n-2)
def InterFibo(n):
    i = 0
    x = 0
    y = 1
    while i < n-1 :
        i += 1
        x += y
        z = x
        x = y
        y = z
    return (z)
while True :
    num = int(input("Enter the number: "))
    if num <= 0 :
        break
    ts = time.time()
    Fibo = Fibo(num)
    ts = time.time() - ts
    print("Fibo(%d)=%d , time = %.6f"%(num,Fibo,ts))
    ts = time.time()
    interFibo = InterFibo(num)
    ts = time.time() - ts
    print("InterFibo(%d)=%d , time = %.6f"%(num,interFibo,ts))

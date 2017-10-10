import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    fibolist = [0,1]
    for i in range(n-1):
        fibolist.append(fibolist[i]+fibolist[i+1])
    return fibolist[n]

while True:
    try:
        nbr = int(input("Enter a number: "))
        if nbr < 0:
            break
        ts = time.time()
        fibonumber = iterfibo(nbr)
        ts = time.time() - ts
        print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
        ts = time.time()
        fibonumber = fibo(nbr)
        ts = time.time() - ts
        print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber,ts))
    except ValueError:
        print("Error")
        break

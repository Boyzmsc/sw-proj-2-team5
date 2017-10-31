import time

def iterfibo(a):
    fn = 0
    sn = 1
    result = 0
    for i in range(a):
        fn = sn
        sn = result
        result = fn + sn
    return result

def fibo(s):
    try :
        if s <=1:
            return s
        return fibo(s-1) + fibo(s-2)
    except ValueError:
        print("Error")
        exit()

n = int(input("N : "))
fibo_result = 0
iterfibo_result = 0

if n == -1:
    exit()

ts = time.time()
fibo_result = fibo(n)
ts = time.time() - ts
print("fibo time : %.6f, Value : %d" %(ts, fibo_result))

ts = time.time()
iterfibo_result = iterfibo(n)
ts = time.time() - ts
print("iterfibo time : %.6f, Value : %d" %(ts, iterfibo_result))
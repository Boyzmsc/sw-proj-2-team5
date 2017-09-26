def Combination(m,n):
    if m >= 0 and n >= 0 and m >= n:
        if n == 0 or m == n:
            return 1
        else:
            return Combination(m - 1, n - 1) + Combination(m - 1, n)
    elif m == 0 and n >= 0:
        if n > m:
            return 0
        else:
            return 1
    else:
        print("Error")
        quit()
while True:
    try:
        m = int(input("m = "))
        n = int(input("n = "))
        print("C(%d,%d) = %d" %(m,n,Combination(m,n)))
    except ValueError:
        print("TypeError")

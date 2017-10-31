def factorialn(x):
    sum = 1
    while x > 0:
        for i in range(1,x+1):
            sum *= i
        return(sum)
        break

n = int(input("Enter n: "))
m = int(input("Enter m: "))
while n > 0:

    facn = factorialn(n)
    facm = factorialn(m)
    facnm = factorialn(n-m)

    result = facn/(facm*facnm)
    print("C(",n,",",m,") = ",result)

    n = int(input("Enter n: "))
    m = int(input("Enter m: "))












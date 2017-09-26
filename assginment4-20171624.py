def combination(n,m):
    return 1 if n == 1 or m == 0 or n == m else combination(n-1,m) + combination(n-1,m-1)

def factorial(n):
    result = 1
    while n > 0:
        for i in range(1, n + 1):
            result = result * i
            n = n - 1
    return result

def factorial_combination(n,m):
    return(factorial(n)/(factorial(m)*factorial(n-m)))

while True:
    try:
        num0 = int(input("n값을 입력하시오: "))
        if num0 == -1:
            break
        num1 = int(input("m값을 입력하시오: "))
        if num1 > num0:
            print("n과 m값이 잘못되었습니다.")
        else:
            ans0 = combination(num0,num1)
            print(ans0)
            ans1 = factorial_combination(num0,num1)
            print(ans1)
    except ValueError:
        print("valueError")

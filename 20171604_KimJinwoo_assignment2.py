try:
    n = int(input("Enter a number: "))
    sum = 1
    while True:
        if n == -1:
            break
        elif n < -1:
            print("Error")
            break
        for i in range(1, n + 1):
            sum = sum * i
        print("%d!" % n, " = ", sum)
        sum = 1
        n = int(input("Enter a number: "))
except ValueError:
    print("Error")

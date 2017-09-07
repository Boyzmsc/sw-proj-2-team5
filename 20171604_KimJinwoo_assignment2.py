"""
KMUSW
Software Project2
Assignment2
20171604 KimJinwoo
"""

try:
    n = int(input("Enter a number: "))
    sum = 1
    while n >= 0:
        for i in range(1, n + 1):
            sum *= i
        print("%d!" % n, " = ", sum)
        sum = 1
        n = int(input("Enter a number: "))
    if n <= -1:
        print("Error")
except ValueError:
    print("Error")

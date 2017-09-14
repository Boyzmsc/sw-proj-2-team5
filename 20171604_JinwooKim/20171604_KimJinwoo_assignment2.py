"""
KMUSW
Software Project2
Assignment2
20171604 KimJinwoo
"""

try:
    num = int(input("Enter a number: "))
    sum = 1
    while num >= 0:
        for i in range(1, num + 1):
            sum *= i
        print("%d!" % num, " = ", sum)
        sum = 1
        num = int(input("Enter a number: "))
    if num <= -1:
        print("Error")
except ValueError:
    print("Error")



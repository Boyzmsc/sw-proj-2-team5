"""
KMUSW
Software Project2
Assignment4
20171604 KimJinwoo

Combination.
"""

def fac(a):
    if a == 1:
        return 1
    else:
        return a * fac(a-1)

n = int(input("Enter n: "))
m = int(input("Enter m: "))

result = fac(n) / (fac(m)*fac(n-m))
print("C(%d,%d) = %d "%(n,m,result))

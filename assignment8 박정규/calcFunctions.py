from math import factorial as fact

def calcselect(key,num):
    if key == 0:
        val = factorial(str(num))
        return val
    elif key == 1:
        val = decToBin(str(num))
        return val
    elif key == 2:
        val = binToDec(str(num))
        return val
    elif key == 3:
        val = decToRoman(str(num))
        return val


def factorial(numStr):
    try:
        numStr = str(eval(numStr))
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        numStr = str(eval(numStr))
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        numStr = str(eval(numStr))
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'

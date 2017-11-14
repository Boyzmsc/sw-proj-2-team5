
def call(n,num):
    if n == 1:
        return factorial(num)
    elif n == 2:
        return decToBin(num)
    elif n == 3:
        return binToDec(num)
    elif n == 4:
        return decToRoman(num)

def factorial(numStr):
    try:
        n = int(numStr)
        if n == 0:
            return 1
        elif n == 1:
            return n
        elif n < 0:
            return "ValueError"
        else:
            return factorial(n - 1) * n
    except:
        return 'Error!'

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'






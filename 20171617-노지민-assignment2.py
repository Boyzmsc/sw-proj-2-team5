y = 1
x = int(input("Enter a number = "))
while x != -1:
  for i in range(1,x+1):  
    y *= i
    print (x,"! = ", y)
    y = 1
    x = int(input("Enter a number = "))

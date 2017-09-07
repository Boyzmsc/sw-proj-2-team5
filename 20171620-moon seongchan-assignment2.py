a = int(input("Enter a number:"))
while a >= 0:
    j = 1
    for k in range (1, a+1):
        j = j*k
    print("%d!= %d"%(a,j))
    a = int(input("Enter a number:"))
if a == -1:
    print("Error")
    

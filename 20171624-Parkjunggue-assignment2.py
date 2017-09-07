num = 0
result = 1

while num != -1:
    result = 1
    num = int(input("수를 입력하시오:"))
    if num == 0:
        print("1")
    elif num > 0:
        for i in range (num) :
            result = result * num
            num = num - 1
        print(result)
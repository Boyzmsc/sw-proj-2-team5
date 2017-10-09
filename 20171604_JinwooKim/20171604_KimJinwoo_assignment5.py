import time
n = int(input("N : "))
fn = 0
sn = 1
result = 0
if n == -1:
    exit()
ts =time.time()
for i in range(n):
    fn = sn
    sn = result
    result = fn + sn
ts = time.time()- ts
print(result,ts)

import time
start = time.time()
n = int(input())
print((n-1)*n//2+(n-2)*(n-1)//2)
print(time.time() - start)


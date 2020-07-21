import sys
sys.stdin = open('input.txt','r')

n, k = map(int, input().split())
array = [0]*(n+1)
array[0] = 1
cnt = 0
for i in range(2,n+1):
    for j in range(1,n):
        if i*j > n or array[i*j]:
            continue
        cnt += 1
        array[i*j] = 1
        if cnt == k:
            print(i*j)
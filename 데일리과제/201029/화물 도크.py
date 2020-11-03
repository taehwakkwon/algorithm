import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    dock = []
    for i in range(n):
        dock.append(tuple(map(int,input().split())))
    dock = sorted(dock, key=lambda x:x[1])
    cnt = 1
    end = dock[0][1]
    for i in range(1,len(dock)):

        if end <= dock[i][0]:
            end = dock[i][1]
            cnt += 1
    print('#%d %d' %(t,cnt))

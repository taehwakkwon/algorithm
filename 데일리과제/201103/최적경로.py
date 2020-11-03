import sys
sys.stdin = open('input.txt')


def dfs(v,x,y, cost):
    global m
    if m <= cost:
        return
    if v == len(info):
        cost += abs(x-home[0]) + abs(y-home[1])
        m = min(m, cost)
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                a, b = info[i]
                dfs(v+1, a, b, cost + abs(x-a)+abs(y-b))
                check[i] = 0


T = int(input())
for t in range(1, T+1):
    n = int(input())
    inp = list(map(int, input().split())) #회사, 집, 고객
    info = []
    for i in range(0,len(inp),2):
        a, b = inp[i:i+2]
        info.append((a,b))

    company = info[0]
    home = info[1]
    info = info[2:]

    check = [0] * n
    m = float('inf')

    dfs(0, company[0], company[1], 0)

    print('#%d %d' %(t, m))


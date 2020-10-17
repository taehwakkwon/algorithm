import sys
sys.stdin = open('../now/input.txt')

def dfs(v,s):
    global m
    if v > 12:
        return
    if v == 12:
        m = min(m,s)
        return
    else:
        if schedule[v] == 0:
            dfs(v+1,s)
        dfs(v + 1, s + schedule[v] * price[0])
        dfs(v + 1, s + price[1])
        dfs(v + 3, s + price[2])


T = int(input())
for t in range(1,T+1):
    #일, 1개월, 3개월, 1년
    price = list(map(int, input().split()))
    schedule = list(map(int, input().split()))
    m = price[-1]
    dfs(0,0)
    print('#%d %d'%(t, m))

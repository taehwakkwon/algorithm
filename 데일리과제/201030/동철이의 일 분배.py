import sys
sys.stdin = open('input.txt')

def round(number):


def dfs(v,p):
    global M
    if p <= M:
        return
    if v == n:
        M = max(M, p)
        return
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            dfs(v+1,p*(probabiliry_box[v][i])/100)
            check[i] = 0


T = int(input())
for t in range(1, T+1):
    n = int(input())
    probabiliry_box = [list(map(int, input().split())) for _ in range(n)]
    M = -float('inf')
    check = [0]*n
    dfs(0,100)
    print('#%d %f' %(t,round(M,7)))

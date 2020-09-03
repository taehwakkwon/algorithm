import sys
sys.stdin = open('sample_input.txt')

def dfs(r,cnt):
    global min_num
    if r >= n:
        if cnt < min_num:
            min_num = cnt
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                dfs(r + 1, cnt + num[r][i])
                visited[i] = 0
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    min_num = 100000
    dfs(0,0)
    print('#%d %d' %(tc, min_num))
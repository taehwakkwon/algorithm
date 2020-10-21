import sys
sys.stdin = open('input.txt')
move = [(0,1),(1,0),(0,-1),(-1,0)]
import time
start = time.time()
sys.setrecursionlimit(10**7)
def dfs(r,c):
    global flag
    for dr, dc in move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if pool[r][c] >= pool[nr][nc] and (nr,nc) not in visited:
                visited.add((nr,nc))
                dfs(nr,nc)
        else:
            flag = False


n, m = map(int, input().split())
pool = [list(map(int, input())) for _ in range(n)]
cnt = 0
for h in range(1,10):
    visited = set([])
    flag = True
    for i in range(n):
        for j in range(m):
            if pool[i][j] < h:
                dfs(i,j)
                visited.add((i, j))
                if flag:
                    for r, c in visited:
                        pool[r][c] += 1
                        cnt += 1
                # for rr in pool:
                #     print(rr)
                # print()
print(cnt)
print(time.time()-start)
#

import sys
sys.stdin = open('sample_input.txt')
def dfs():
    global min_cnt, result
    dr = [0,0,1]
    dc = [-1,1,0]
    for i in range(len(ladder)):
        if ladder[0][i]==1:
            visited = [[0]*100 for _ in range(100)]
            stack = []
            stack.append((0,i))
            cnt = 1
            while stack:
                cr, cc = stack.pop()
                visited[cr][cc] = 1
                for d in range(3):
                    nr = cr+dr[d]
                    nc = cc+dc[d]
                    if 0 <= nr < 100 and 0 <= nc < 100 and not visited[nr][nc] and ladder[nr][nc]==1:
                        stack.append((nr,nc))
                        cnt += 1
                        if nr == 99:
                            if min_cnt > cnt:
                                min_cnt = cnt
                                result = i
                        break
t = 10
for tc in range(1,11):
    n = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    min_cnt = 10000
    result = 0
    dfs()
    print('#%d %d' %(tc, result))
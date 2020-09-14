import sys
sys.stdin = open('input.txt')

def dfs():
    global box
    dr = [-1,1,0,0] #상하좌우
    dc = [0,0,-1,1]
    visited = [[0] * (M) for _ in range(N)]
    stack = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1 and visited[i][j] == 0:
                stack.append((i,j))
                cnt += 1
                while stack:
                    cr,cc = stack.pop()
                    visited[cr][cc] = 1
                    for d in range(4):
                        nr = cr+dr[d]
                        nc = cc+dc[d]
                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                            if box[nr][nc] == 1:
                                stack.append((nr,nc))
    return cnt


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    # arr = [list(map (int, input().split())) for _ in range(K)]
    box = [[0]* (M) for _ in range(N)]
    for i in range(K):
        x,y = map(int, input().split())
        box[y][x] = 1
    print(dfs())
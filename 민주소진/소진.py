import sys
sys.stdin = open('input.txt')


def DFS(r, c):
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]: #우하좌상
        if 0 <= r + dr < R and 0 <= c + dc < C and Board[r+dr][c+dc] == '#' and visited[r+dr][c+dc] == 0:
            visited[r+dr][c+dc] = 1
            DFS(r+dr,c+dc)


R, C = map(int, input().split())
Board = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
cnt = 0
for i in range(R):
    for j in range(C):
        if Board[i][j] == '#' and visited[i][j] == 0:
            DFS(i, j)
            cnt += 1
print(cnt)
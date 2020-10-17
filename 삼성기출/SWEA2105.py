import sys
sys.stdin = open('../now/input.txt')

move = [(1,1),(1,-1),(-1,-1),(-1,1)]
def dfs(r,c,direc,s):
    global M
    if direc >= 4:
        return
    if (r,c) == (i,j) and s >= 4:
        M = max(M, s)
    else:
        nr, nc = r + move[direc][0], c + move[direc][1]
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and numbers[board[nr][nc]] == 0:
            visited[nr][nc] = numbers[board[nr][nc]] = 1
            dfs(nr, nc, direc,s+1)
            dfs(nr, nc, direc+1, s + 1)
            visited[nr][nc] = numbers[board[nr][nc]] = 0


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    M = -float('inf')
    for i in range(n-2):
        for j in range(1, n):
            visited = [[0]*n for _ in range(n)]
            numbers = [0]*101
            dfs(i,j,0,0)
    if M == -float('inf'):
        print('#%d %d' %(t,-1))
    else:
        print('#%d %d' %(t,M))


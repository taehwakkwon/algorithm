import sys
sys.stdin = open('../now/input.txt')

def dfs(y,x):
    for dr, dc in [(0,1), (1,0),(0,-1), (-1,0)]:
        if 0 <= y + dr < r and 0 <= x + dc < c and board[y+dr][x+dc] == '#':
            board[y + dr][x + dc] = '.'
            dfs(y + dr, x + dc)


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
cnt = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == '#':
            cnt += 1
            dfs(i,j)
print(cnt)
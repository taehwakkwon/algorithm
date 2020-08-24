import sys
sys.stdin = open('input.txt')
import sys
sys.setrecursionlimit(10**7)
def dfs(v,l):
    if v < 0 and v >= H and l < 0 and l >= W:
        return
    else:
        for dy, dx in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if 0 <= v + dy < H and 0 <= l + dx < W:
                y, x = v + dy, l + dx
                if board[y][x] == '#':
                    board[y][x] = '.'
                    dfs(y,x)


T = int(sys.stdin.readline())
for t in range(T):
    H, W = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == "#":
                cnt += 1
                dfs(i,j)
    print(cnt)




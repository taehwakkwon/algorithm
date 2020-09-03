#import sys
#sys.stdin = open('sample_input.txt')

def dfs(i,j,s):
    global res
    if board[i][j] == 3:
        res = 1
        return
    else:
        board[i][j] = 1
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r = i + dr
            c = j + dc
            if 0 <= r < n and 0 <= c < n and board[r][c] != 1:
                dfs(r, c, s + 1)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                start = (i, j)

    board[start[0]][start[1]] = 1
    dfs(start[0],start[1])

    print('#%d %d'%(t, res))


import sys
sys.stdin = open('input.txt')


def dfs(start, r, c, s):
    global M, val
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < n and 0 <= new_c < n and board[r][c] == board[new_r][new_c] - 1:
            dfs(start, new_r, new_c, s + 1)

    if s == M:
        M = s
        val = min(board[start[0]][start[1]],val)
    elif s > M:
        M = s
        val = board[start[0]][start[1]]


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    M = 0
    val = float('inf')
    for i in range(n):
        for j in range(n):
            dfs((i, j), i, j, 1)
    print('#%d' % (t), val, M)
import sys
sys.stdin = open('input.txt')

def dfs(v):
    for i in range(n + 1):
        if board[v][i] == 1:
            board[v][i] = board[i][v] = 0
            check[v] = check[i] = 1
            dfs(i)


T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        board[i][i] = 1
    check = [0] * (n + 1)
    cnt = 0
    for i in range(m):
        a, b = map(int, input().split())
        board[a][b] = board[b][a] = 1

    for i in range(1, n + 1):
        if check[i] == 0:
            dfs(i)
            cnt += 1

    print('#%d %d' %(t, cnt))

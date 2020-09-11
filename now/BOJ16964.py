import sys
sys.stdin = open('../DFS_BFS/input.txt')

def dfs(v):
    global res
    print(v, end = ' ')
    res += str(v)
    if v == n:
        result.append(res)
        res = ''
        return
    else:
        # for r in board:
        #     print(*r)
        # print(route[v], route[v+1], board[route[v]][route[v+1]])
        if board[route[v]][route[v+1]] == 1:
            board[route[v]][route[v + 1]] = 0
            dfs(route[v + 1])

        # else:
        #     for i in range(1, n + 1):
        #         if board[route[v]][i] == 1:
        #             board[route[v]][i] = 0
        #             dfs(i)
        #     return



        for i in range(n + 1):
            if board[v][i] == 1:
                board[v][i] = 0
                dfs(i)
                board[v][i] = 1

result = []
n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
for i in range(n-1):
    r, c = map(int,input().split())
    board[r][c] = 1
    board[c][r] = 1
route = [0] + list(map(int, input().split()))
res = ''
dfs(1)
print()
print(result)


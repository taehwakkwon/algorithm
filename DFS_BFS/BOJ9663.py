from copy import deepcopy
def check(i, j, y, x, d, v):
    if d == 8:
        dfs(v + 1)
        return
    y += move[d][0]
    x += move[d][1]
    if 0 <= y < N and 0 <= x < N:
        if board[y][x] == 0:
            board[y][x] = -1
            check(i, j, y, x, d, v)
            board[y][x] = 0
        elif board[y][x] == -1:
            check(i, j, y, x, d, v)
            board[y][x] = -1
    else:
        return


def dfs(v):
    if v == N:
        res.append(deepcopy(board))
        return
    else:
        rsum = 0
        for i in range(len(board)):
            rsum += board[i].count(0)
        if rsum < N - v:
            return
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    check(i,j,i,j,0,v)
                    for r in board:
                        print(r)
                    print()


res = []
move = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
N = 4#int(input())
for i in range(N):
    for j in range(N):
        board = [[0] * N for _ in range(N)]
        if board[i][j] == 0:
            dfs(0)
print(res)
print(len(set(res)))


import sys
sys.stdin = open('../now/input.txt')

import sys
sys.setrecursionlimit(10**7)
from copy import deepcopy
def move(d,board):
    global M
    new_board = deepcopy(board)
    #상하좌우
    if d == 0:
        for i in range(n):
            for j in range(n - 1):
                if new_board[j][i] == 0:
                    for k in range(j+1, n):
                        if new_board[k][i]:
                            new_board[j][i], new_board[k][i] = new_board[k][i], new_board[j][i]
                            break
            for j in range(n-1):
                if new_board[j][i] == new_board[j+1][i]:
                    new_board[j][i] *= 2
                    new_board[j+1][i] = 0
            else:
                for j in range(n-1):
                    if new_board[j][i] == 0:
                        for k in range(j, n):
                            if new_board[k][i]:
                                new_board[j][i], new_board[k][i] = new_board[k][i], new_board[j][i]
                                break

    if d == 1:
        for i in range(n):
            for j in range(n - 1, 0, -1):
                if new_board[j][i] == 0:
                    for k in range(j, -1, -1):
                        if new_board[k][i]:
                            new_board[j][i], new_board[k][i] = new_board[k][i], new_board[j][i]
                            break
            for j in range(n-1,0,-1):
                if new_board[j][i] == new_board[j-1][i]:
                    new_board[j][i] *= 2
                    new_board[j-1][i] = 0
            else:
                for j in range(n-1,0,-1):
                    if new_board[j][i] == 0:
                        for k in range(j, -1, -1):
                            if new_board[k][i]:
                                new_board[j][i], new_board[k][i] = new_board[k][i], new_board[j][i]
                                break
    if d == 2:
        for i in range(n):
            for j in range(n-1):
                if new_board[i][j] == 0:
                    for k in range(j,n):
                        if new_board[i][k]:
                            new_board[i][j], new_board[i][k] = new_board[i][k], new_board[i][j]
                            break
            for j in range(n-1):
                if new_board[i][j] == new_board[i][j+1]:
                    new_board[i][j] *= 2
                    new_board[i][j+1] = 0

            for j in range(n-1):
                if new_board[i][j] == 0:
                    for k in range(j,n):
                        if new_board[i][k]:
                            new_board[i][j], new_board[i][k] = new_board[i][k], new_board[i][j]
                            break
    if d == 3:
        for i in range(n):
            for j in range(n - 1, 0, -1):
                if new_board[i][j] == 0:
                    for k in range(j, -1,-1):
                        if new_board[i][k]:
                            new_board[i][j], new_board[i][k] = new_board[i][k], new_board[i][j]
                            break
            for j in range(n-1,0,-1):
                if new_board[i][j] == new_board[i][j-1]:
                    new_board[i][j] *= 2
                    new_board[i][j-1] = 0
            else:
                for j in range(n-1,0,-1):
                    if new_board[i][j] == 0:
                        for k in range(j, -1, -1):
                            if new_board[i][k]:
                                new_board[i][j], new_board[i][k] = new_board[i][k], new_board[i][j]
                                break
    for i in range(n):
        if max(new_board[i]) > M:
            M = max(new_board[i])
    return new_board

def dfs(v,board):
    if v >= 5:
        return
    else:
        for i in range(4):
            new_board = move(i,board)
            if new_board not in visited:
                visited.append(new_board)
                visited_cnt.append(v)
                dfs(v + 1, new_board)
            else:
                if v < visited_cnt[visited.index(new_board)]:
                    visited_cnt.pop(visited.index(new_board))
                    visited.remove(new_board)
                    visited.append(new_board)
                    visited_cnt.append(v)
                    dfs(v + 1, new_board)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
M = 0

visited = [[board]]
visited_cnt = [0]
dfs(0,board)
print(M)
import sys
sys.stdin = open('input.txt')

from collections import deque
from copy import deepcopy
def move(d):
    global M
    new_board = deepcopy(board)
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


def bfs(queue, c):
    global board
    if c >= 5:
        return M
    next_queue = deque([])
    while queue:
        board = queue.popleft()
        for d in range(4):
            new_board = deepcopy(move(d))
            # for r in new_board:
            #     print(r)
            # print(c)
            # print(M)
            if new_board not in visited:
                visited.append(new_board)
                next_queue.append(new_board)
    if next_queue:
        bfs(next_queue, c + 1)
    else:
        return M

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
M = 0
queue = deque([board])
visited = [[board]]
bfs(queue,0)
print(M)
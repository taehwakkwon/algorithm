import sys
sys.stdin=open('input.txt')

import time
start = time.time()
move = [(0,1), (0,-1),(-1,0),(1,0)]
T = int(input())
CNTER = 200
for t in range(1, T+1):
    n, m, k = map(int, input().split())
    board = [[0]*(2*CNTER) for _ in range(2*CNTER)]

    inputs = [list(map(int, input().split())) for _ in range(n)]
    cells = []
    for i in range(n):
        for j in range(m):
            if inputs[i][j] != 0:
                cells.append([False, CNTER+i,CNTER+j, inputs[i][j]])

    for i in range(n):
        for j in range(m):
            board[CNTER+i][CNTER+j] = inputs[i][j]

    for hour in range(k):
        idx = 0
        while idx < len(cells):
            if cells[idx][0] == True:
                if cells[idx][3] == 1:
                    x, y = cells[idx][1:3]
                    cells.pop(idx)
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if board[x][y] > board[nx][ny]:
                            board[nx][ny] = board[x][y]
                            cells.append([False,nx,ny,board[x][y]])
                else:
                    cells[idx][3] -= 1
                    idx += 1
            else:# cells[idx][0] == False:
                #deactivated
                if cells[idx][3] == 1:
                    cells[idx][0] = True
                else:
                    cells[idx][3] -= 1
                idx += 1


        print(cells)
        print(hour)
        print(len(cells))
    break




print(time.time()-start)
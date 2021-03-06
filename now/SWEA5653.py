import sys
sys.stdin = open('input.txt')
import time
from collections import deque, defaultdict

#활성상태인 시점에

T = int(input())
for t in range(1, T+1):
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    activated = deque([[] for _ in range(301)])
    deactivated = deque([[] for _ in range(301)])
    cells = {}
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                deactivated[board[i][j]].append([i,j,board[i][j]])
                cells[(i,j)] = -board[i][j]
    # print(deactivated)
    # print(activated)
    # print()
    for i in range(k+1):
        for acts in activated:
            for act in acts:
                x,y,k = act
                for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nx, ny = x+dx, y+dy
                    if (nx,ny) in cells:
                        if k > cells[(nx,ny)] > 0:
                            if [nx,ny,cells[(nx,ny)]] in deactivated[cells[(nx,ny)]]:
                                deactivated[cells[(nx, ny)]].remove([nx,ny,cells[(nx,ny)]])
                            deactivated[k].append([ny,nx,k])
                            cells[(nx, ny)] = k
                    else:
                        cells[(nx,ny)] = k
                        deactivated[k].append([nx,ny,k])
                cells[(x,y)] = 0
        acts = activated.popleft()
        deacts = deactivated.popleft()
        for left in deacts:
            activated[left[2]-1].append(left[:])
            cells[(left[0],left[1])] = (-1)*cells[(left[0],left[1])]

        # print(deactivated)
        # print(activated)
        #
        # cnt = 0
        # for p in activated:
        #     for q in p:
        #         cnt += 1
        # for p in deactivated:
        #     for q in p:
        #         cnt += 1
        # print(cnt, i)

    cnt = 0
    for i in activated:
        for j in i:
            cnt += 1
    for i in deactivated:
        for j in i:
            cnt += 1
    print(cnt)



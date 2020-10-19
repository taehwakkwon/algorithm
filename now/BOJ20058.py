import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(r,c):
    queue = deque([(r,c)])
    visited[r][c] = 1
    count = 1
    while queue:
        r,c  = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and visited[nr][nc] == 0 and board[nr][nc] > 0:
                queue.append((nr,nc))
                visited[nr][nc] = 1
                count += 1
    return count


def update(a,b):
    for idx in range(BOARD_SIZE):
        for jdx in range(BOARD_SIZE):
            a[idx][jdx] = b[idx][jdx]

move = [(0,1),(1,0),(0,-1),(-1,0)]
n, q = map(int, input().split())

BOARD_SIZE = 2**n
board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]
levels = list(map(int, input().split()))
#1 -> 2^1

for level in levels:
    if level > 0:
        next_board = [[0]*BOARD_SIZE for _ in range(BOARD_SIZE)] #얘 한칸 떙겨두댐..
        box_size = 2**level
        inner_size = 2**(level-1)
        #rotate
        for r in range(0, BOARD_SIZE, box_size):
            for c in range(0, BOARD_SIZE, box_size):
                br, bc = r, c
                for dr, dc in move:
                    nr, nc = br+dr*inner_size, bc + dc*inner_size
                    print(nr,nc)
                    for idx in range(inner_size):
                        for jdx in range(inner_size):
                            next_board[nr+idx][nc+jdx] = board[br+idx][bc+jdx]
                    br, bc = nr,nc

        update(board,next_board)
    else:
        next_board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        update(next_board, board)

    for rr in board:
        print(rr)
    print(level)


    for idx in range(BOARD_SIZE):
        for jdx in range(BOARD_SIZE):
            if board[idx][jdx] > 0:
                cnt = 0
                for dr, dc in move:
                    nr, nc = idx + dr, jdx + dc
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] > 0:
                        cnt += 1

                if cnt < 3:
                    # print(idx,jdx)
                    next_board[idx][jdx] -= 1
    update(board, next_board)
    # for rr in board:
    #     print(rr)
    # print(level)

visited = [[0]*BOARD_SIZE for _ in range(BOARD_SIZE)]
total = 0
M = 0

for idx in range(BOARD_SIZE):
    for jdx in range(BOARD_SIZE):
        if board[idx][jdx] > 0:
            total += board[idx][jdx]
            if visited[idx][jdx] == 0:
                M = max(M, bfs(idx,jdx))

print(total, M, sep='\n')
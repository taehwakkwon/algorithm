import sys
sys.stdin = open('../now/input.txt')
from collections import deque
def bfs():
    visited = {}
    visited[tuple(queue[0][1:])] = 0

    while queue:
        c, r_r, r_c, b_r, b_c = queue.popleft()
        print(c,r_r, r_c, b_r, b_c)
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr_r, nr_c = r_r,r_c
            nb_r, nb_c = b_r,b_c
            board[r_r][r_c] = 'R'
            board[b_r][b_c] = 'B'

            for _ in range(max(m,n)):
                if board[nr_r+dr][nr_c+dc] == '.':
                    board[nr_r][nr_c] = '.'
                    nr_r+=dr
                    nr_c+=dc
                    board[nr_r][nr_c] = 'R'

                elif board[nr_r+dr][nr_c+dc] == 'O':
                    board[nr_r][nr_c] = '.'
                    nr_r = nr_c = -1

                if board[nb_r+dr][nb_c+dc] == '.':
                    board[nb_r][nb_c] = '.'
                    nb_r+=dr
                    nb_c+=dc
                    board[nb_r][nb_c] = 'B'
                elif board[nb_r+dr][nb_c+dc] == 'O':
                    board[nb_r][nb_c] = '.'
                    nb_r = nb_c = -1
                if (nb_r, nb_c) == (nr_r,nr_c) == (-1,-1):
                    break
            else:
                board[nr_r][nr_c] = board[nb_r][nb_c] = '.'
                if (nr_r,nr_c) == (-1,-1):
                    return c + 1
                if c + 1 > 10:
                    continue
                elif (nr_r,nr_c,nb_r,nb_c) not in visited:
                    visited[(nr_r,nr_c,nb_r,nb_c)] = 0
                    queue.append((c+1, nr_r,nr_c,nb_r,nb_c))
    return -1


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
blue = []
red = [0]
for i in range(n):
    if 'R' in board[i]:
        red.extend([i,board[i].index('R')])
    if 'B' in board[i]:
        blue.extend([i,board[i].index('B')])
red.extend(blue)
queue = deque([tuple(red)])
print(bfs())
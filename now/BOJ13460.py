import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs():
    while queue:
        c, r_r, r_c, b_r,b_c = queue.popleft()
        if c > 10:
            return -1
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]: #우하좌상
            while (0 <= r_r + dr < n and 0 <= r_c + dc < m and board[r_r+dr][r_c+dc] =! '#') or (0 <= b_r + dr < n and 0 <= b_c + dc < m and board[b_r+dr][b_c+dc] != '#'):
                if board[r_r+dr][r_c+dc] == 'O':
                    return c + 1
                if board[r_r+dr][r_c+dc] == '.' and board[]





            while :
                if 0 <= b_r + dr < n and 0 <= b_c + dc < m:
                    if board[b_r + dr][b_c+dc] == 'O':
                        break
                    elif board[b_r+dr][b_c+dc] == '.':
                        b_r += dr
                        b_c += dc

                if 0 <= r_r + dr < n and 0 <= r_c + dc < m:
                    if board[r_r + dr][r_c+dc] == 'O':
                        return c + 1
                    elif board[r_r+dr][r_c+dc] == '.':
                        r_r += dr
                        r_c += dc
                print(r_r,r_c)
            else:
                red.append((c+1,r_r,r_c))
                blue.append((c+1,b_r,b_c))

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
queue = deque(red)
print(queue)
#print(bfs())
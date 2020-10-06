import sys
sys.stdin = open('input.txt')

from collections import deque
from itertools import combinations
def check():
    queue = deque(virus)
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < n and 0 <= new_c < m and board[new_r][new_c] == 0:
                board[new_r][new_c] = 2
                queue.append((new_r,new_c))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
            elif board[i][j] == 2 and (i,j) not in virus:
                board[i][j] = 0
    return cnt

wall = 3
comb = []
M = 0
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = set([])
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.add((i,j))

numbers = [(i,j) for i in range(n) for j in range(m)]
comb = list(combinations(numbers, 3))
for a, b, c in comb:
    if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] == 0:
        board[a[0]][a[1]] = board[b[0]][b[1]] = board[c[0]][c[1]] = 1
        M = max(check(),M)
        board[a[0]][a[1]] = board[b[0]][b[1]] = board[c[0]][c[1]] = 0
print(M)

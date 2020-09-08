import sys
sys.stdin = open('input.txt')




from collections import deque
def bfs(r,c):
    queue = deque([(1, r,c)])
    visited = [[0]*n for _ in range(n)]
    while queue:
        s, r, c = queue.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < n and 0 <= new_c < n and board[new_r][new_c] - 1 == board[r][c] and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                queue.append((s + 1, new_r, new_c))
                visited[new_r][new_c] = 0
    return s




T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    M = 0
    start = float('inf')
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = bfs(i,j)
            if s >= M:
                M = s
                start = min(start, board[i][j])
    print('#%d'%(t), start, M)


#1 6 8
#2 2 2
#3 1 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 1 2
#10 1 35
#11 1 2
#12 4 2
#13 1 2
#14 2 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 13 2
#20 7 14
#21 2 2
#22 225 2200
#23 6 3
#24 2 2
#25 2 2
#26 6 2
#27 5 5
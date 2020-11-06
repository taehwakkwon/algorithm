import sys
sys.stdin = open('input.txt')


from heapq import *
move = [(0,1),(1,0),(-1,0),(0,-1)]
for t in range(1, int(input())+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    cost = 0
    result = [[float('inf')]*n for _ in range(n)]
    result[0][0] = 0


    queue = []
    heappush(queue, (0,0,0))

    while queue:
        w, r, c = heappop(queue)
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and result[nr][nc] > (result[r][c] + board[nr][nc]):
                result[nr][nc] = result[r][c] + board[nr][nc]
                heappush(queue, (result[nr][nc], nr, nc))

    print('#%d %d' %(t, result[n-1][n-1]))



import sys
sys.stdin = open('input.txt')

import sys
from collections import deque
def search(row, col, goto_destination, row_des, col_des):
    global fuel
    if sum(passenger_check) == M:
        return
    q = deque([])
    q.append((row, col, 0))
    visited = set([])
    while q:
        current = q.popleft()
        r, c, f = current[0], current[1], current[2]
        visited.add((r,c))
        if not goto_destination and (r, c) in passenger and not passenger_check[passenger.index((r,c))]:
            xr, xc = destination[passenger.index((r,c))]
            if fuel >= f:
                fuel -= f
                return search(r, c, True, xr, xc)
            else:
                fuel = -1
                return
        if goto_destination and (r, c) == (row_des, col_des):
            passenger_check[destination.index((r,c))] = True
            if fuel >= f:
                fuel += f
                return search(r, c, False, -1, -1)
            else:
                fuel = -1
                return
        for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
            nr, nc = r+dr, c+dc
            if not(1 <= nr <= N) or not(1 <= nc <= N) or arr[nr][nc] or (nr,nc) in visited:
                continue
            q.append((nr,nc,f+1))
    fuel = -1
    return
N, M, fuel = map(int, sys.stdin.readline().split())
arr = list([0] + list(map(int, sys.stdin.readline().split())) for _ in range(N))
arr = [[0]*(N+1)] + arr
start_row, start_col = map(int, sys.stdin.readline().split())
passenger_check = [False] * M
passenger = []
destination = []
for _ in range(M):
    a, b, c, d = map(int, sys.stdin.readline().split())
    passenger.append((a,b))
    destination.append((c,d))
search(start_row, start_col, False, -1, -1)
print(fuel)
import sys
sys.stdin = open('../now/input.txt')

from collections import deque
def bfs():
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < l and 0 <= new_c < l and board[new_r][new_c] == 0:
                board[new_r][new_c] = board[r][c] + 1
                if (new_r, new_c) == end:
                    return board[new_r][new_c]
                queue.append((new_r,new_c))


T = int(input())
for t in range(1, T + 1):
    l = int(input())
    board = [[0]*l for _ in range(l)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start == end:
        print(0)
    else:
        print(bfs())
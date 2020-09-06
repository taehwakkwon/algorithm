import sys
sys.stdin = open('input.txt')

from collections import deque
from copy import deepcopy
def check(li):
    for i, j in zip(li, board):
        for p, q in zip(i, j):
            if p != q:
                return False
    return True


def bfs(queue):
    global cnt
    cnt += 1
    while queue:
        v = [queue.popleft(), queue.popleft(), queue.popleft()]
        for i in range(3):
            for j in range(3):
                c = deepcopy(v)
                print(queue)
                for dr, dc in [(0,0), (0,1),(1,0),(0,-1),(-1,0)]:
                    new_r, new_c = i + dr, j + dc
                    if 0 <= new_r < 3 and 0 <= new_c < 3:
                        if c[new_r][new_c] == 0:
                            c[new_r][new_c] = 1
                        else:
                            c[new_r][new_c] = 0
                queue.append(c)
                if check(c):
                    return cnt
    else:
        bfs(queue)

T = int(input())
for t in range(T):
    cnt = 0
    board = [list(map(int, input().replace('.','0').replace('*','1'))) for _ in range(3)]
    white = [[0]*3 for _ in range(3)]
    visited = set([])
    queue = deque(white)
    print(bfs(queue))

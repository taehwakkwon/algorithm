#import sys
#sys.stdin = open('input.txt')
from collections import deque
def bfs(l):
    global res
    visited = [l]
    queue = deque([(0,l)])
    while queue:
        c, l = queue.popleft()
        if l == g:
            res = c
            return
        for i in range(1, v + 1):
            if board[l][i] == 1 and i not in visited:
                visited.append(i)
                queue.append((c + 1, i))



T = int(input())
for t in range(1, T + 1):
    res = 0
    v, e = map(int, input().split())
    board = [[0]*(v + 1) for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        board[a][b] = 1
        board[b][a] = 1
    s, g = map(int, input().split())
    res = 0
    bfs(s)
    print('#%d' %t, res)

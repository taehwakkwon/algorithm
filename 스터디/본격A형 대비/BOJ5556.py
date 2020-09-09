import sys
sys.stdin = open('input.txt')
#빨, 파, 노
import time
start = time.time()
from collections import deque
def gen_board(n):
    board = [[0] * (n//2) for _ in range(n//2)]
    r, c = 0, 0
    sr, sc = 0, 0
    n //= 2
    while n:
        print(n)
        for dr, dc in [(1,0),(0,1)]:
            for i in range(n):
                board[r][c] = color[0]
                r += dr
                c += dc
            r -= dr
            c -= dc
        else:
            sr += 1
            sc += 1
            r, c = sr, sc
            c = sc
            n -= 1
            color.rotate(-1)
    return board

color = deque([1,2,3])
n = int(input())
board = gen_board(n)
k = int(input())
res = []
for i in range(k):
    a, b = map(int, input().split())

    #print(board[a - 1][b - 1])

for r in board:
    print(*r)

print(time.time()-start)
# color = deque([1,2,3])
# n = int(input())
# board = gen_board(n)
# k = int(input())
# res = []
# for i in range(k):
#     a, b = map(int, input().split())
#     print(board[a - 1][b - 1])


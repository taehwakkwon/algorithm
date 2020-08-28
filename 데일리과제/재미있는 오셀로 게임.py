import sys
sys.stdin = open('sample_input.txt')

def check(r, c, color):
    for dr, dc in move:
        new_r, new_c = r + dr, c + dc
        while 0 <= new_r < n and 0 <= new_c < n:
            if board[new_r][new_c] == 0:
                break

            if board[new_r][new_c] == color:
                d_r, d_c = new_r,new_c
                while (d_r, d_c) != (r, c):
                    d_r -= dr
                    d_c -= dc
                    board[d_r][d_c] = color
                break
            else:
                new_r += dr
                new_c += dc


move = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0]*n for _ in range(n)]
    board[n//2 - 1][n//2], board[n//2][n//2-1], board[n//2][n//2], board[n//2-1][n//2-1] = 1, 1, 2, 2
    for i in range(m):
        y, x, c = map(int, input().split())
        board[y - 1][x - 1] = c
        check(y - 1, x - 1, c)
    b, w = 0, 0
    for i in range(n):
        b += board[i].count(1)
        w += board[i].count(2)
    print('#%d %d %d' %(tc, b, w))
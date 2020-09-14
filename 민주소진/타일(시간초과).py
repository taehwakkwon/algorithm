import sys
sys.stdin = open('input.txt')

n = int(input())
board = [[0]*n for _ in range(n)]
color = [1,2,3]
for i in range(n//2+1):
    r, c = i, i
    board[r][c] = color[i%3]
    for dr, dc in [(1,0), (0,1),(-1,0),(0,-1)]:
        for j in range(n-2*i-1):
            r += dr
            c += dc
            board[r][c] = color[i%3]

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    print(board[b-1][a-1])
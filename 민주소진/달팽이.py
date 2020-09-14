import sys
sys.stdin = open('input.txt')

n = int(input())
k = int(input())
table = [[0]*n for _ in range(n)]
num = n**2
r,c = 0,0
move = [(1,0),(0,1),(-1,0),(0,-1)]
table[r][c] = num
num -= 1
while num >= 1:
    for dr, dc in move:
        while 0 <= r + dr < n and 0 <= c + dc < n and table[r + dr][c + dc] == 0:
            table[r+dr][c+dc] = num
            num -= 1
            r += dr
            c += dc
for r in table:
    print(*r)
for i in range(n):
    for j in range(n):
        if table[i][j] == k:
            print(i+1, j+1)
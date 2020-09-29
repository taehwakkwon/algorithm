import sys
sys.stdin = open('input.txt')
MAX = 101



def check(min_y, min_x,max_y, max_x):
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            if board[y][x] == 0:
                return False
    return True

n = int(input())
board = [[0]*MAX for _ in range(MAX)]
line = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(10):
        line.extend([(a,b+j),(a+j,b),(a+9-j,b+9),(a+9,b+9-j)])
        for k in range(10):
            board[a+j][b+k] = 1
comb = {}
for i in range(len(line)):
    for j in range(i+1,len(line)):
        cal = (abs(line[i][0] - line[j][0])+1)*(abs(line[i][1]-line[j][1])+1)
        if cal > 100:
            comb[(line[i],line[j])] = cal
M = 100
for loc, area in comb.items():
    min_y, min_x = min(loc[0][0], loc[1][0]), min(loc[0][1], loc[1][1])
    max_y, max_x = max(loc[0][0], loc[1][0]), max(loc[0][1], loc[1][1])
    if check(min_y, min_x,max_y, max_x):
        if M < area:
            M = area
print(M)


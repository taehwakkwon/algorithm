import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**7)

def check(r,c,d):
    if d % 2:
        for dr, dc in [(0, 1),(0, -1)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 102 and 0 <= new_c < 102 and board[new_r][new_c] == False:
                visited[new_r][new_c] = 5
                return True
    else:
        for dr, dc in [(1,0), (-1,0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 102 and 0 <= new_c < 102 and board[new_r][new_c] == False and visited[new_r][new_c] == False:
                visited[new_r][new_c] = 5
                return True
    return False



def dfs(r,c):
    global cnt
    d = 0
    for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
        new_r, new_c = r + dr, c + dc
        if board[new_r][new_c] == True and (check(new_r,new_c,d)):
            #visited[r][c] = 1
            print((new_r,new_c), end = ' ')
            cnt += 1
            dfs(new_r,new_c)
        d += 1





n = int(input())
board = [[0]*102 for _ in range(102)]
visited = [[0]*102 for _ in range(102)]

color = []
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    for i in range(a+1,a+11):
        for j in range(b+1,b+11):
            board[i][j] = 1

for i in range(102):
    for j in range(102):
        if board[i][j] == 1:
            dfs(i,j)
m = 0
for r in visited:
    print(*r)
    m += r.count(5)
print(m)




print(cnt)


import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**8)
def dfs(r, c, color, board):
    if (r,c) == (n-1, n-1):
        return
    else:
        for dr, dc in [(0, 1),(1,0),(0,-1),(-1,0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < n and 0 <= new_c < n and board[new_r][new_c] == color:
                board[new_r][new_c] = 0
                dfs(new_r, new_c, color, board)



n = int(input())
board_normal = []
board_abnormal = []
for i in range(n):
    tmp = input()
    board_normal.append(list(map(int, tmp[:].replace('R','1').replace('G','2').replace('B','3'))))
    board_abnormal.append(list(map(int, tmp[:].replace('R', '1').replace('G', '1').replace('B', '2'))))

normal = 0
abnormal = 0

for i in range(n):
    for j in range(n):
        if board_normal[i][j] != 0:
            dfs(i,j,board_normal[i][j], board_normal)
            normal += 1
        if board_abnormal[i][j] != 0:
            dfs(i, j, board_abnormal[i][j], board_abnormal)
            abnormal += 1
print(normal, abnormal)

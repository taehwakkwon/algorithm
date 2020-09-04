import sys
sys.stdin = open('input.txt')
import time
start = time.time()

def dfs(r, c, v, res):
    if v == 6:
        result[res] = 0
    else:
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < 4 and 0 <= new_c < 4:
                dfs(new_r,new_c,v + 1, res + str(board[new_r][new_c]))


T = int(input())
for t in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    result = {}
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,str(board[i][j]))
    print('#%d %d' %(t,len(result)))
    print(time.time() - start)
import sys
sys.stdin = open('input.txt')

def dfs(r,c,s,flag):
    global longest
    longest = max(longest, s)
    print(r,c,s)
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            if 0 < board[r][c] - board[nr][nc]:
                dfs(nr,nc,s+1,flag)
            if flag:
                for i in range(1,k+1):
                    if board[r][c] > (board[nr][nc]-i):
                        board[r][c] -= i
                        dfs(nr,nc,s+1,False)
                        board[r][c] += i

# from collections import deque
# def bfs():
#     global longest
#     queue = deque(top)
#     while queue:
#         flag, dis, r, c = queue.popleft()
#         print(flag, dis, r, c)
#         for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
#             nr,nc = r+dr, c +dc
#             if 0 <= nr < n and 0 <= nc < n:
#                 if 0 < board[r][c] - board[nr][nc]:
#                     queue.append((flag,dis+1,nr,nc))
#                 elif flag and board[nr][nc] - board[r][c] < k:
#                     queue.append((False, dis+1, nr, nc))
#     longest = max(dis,longest)
#


T = int(input())
for t in range(1,T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    M = 0
    top = []
    longest = 0
    for i in range(n):
        for j in range(n):
            if M < board[i][j]:
                top = [(i,j)]
                M = board[i][j]
            elif M == board[i][j]:
                top.append((i,j))
    for r, c in top:
        dfs(r,c,0,True)
        print()
    #dfs()
    print('#%d %d' %(t, longest))
    break





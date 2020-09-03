import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(v, s):
    global m
    if s > m:
        return
    if v == n:
        if s < m:
            m = s
    else:
        for c in range(n):
            if visited[c] == 0:
                visited[c] = 1
                dfs(v + 1, s + board[v][c])
                visited[c] = 0


T = int(input())
for t in range(1, 1 + T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    m = float('inf')
    dfs(0, 0)
    print(m)



#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def dfs(v,s):
#     if v == m:
#         for i in range(m):
#             print(res[i], end = ' ')
#         print()
#         return
#     else:
#         for i in range(s, n + 1):
#             res[v] = i
#             dfs(v + 1, i + 1)
#
#
# n = 6
# m = 3
# res = [0]*(n + 1)
# dfs(0,1)
# for i in range(1,6):
#     for j in range(i + 1, 6):
#         for k in range(j + 1, 6):
#             print((i, j, k), end = ' ')
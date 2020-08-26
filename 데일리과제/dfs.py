import sys
sys.setrecursionlimit(10**7)
def dfs(v):
    if v > n:
        return
    if v not in visited:
        visited.append(v)
        for i in range(n,-1,-1):
            if board[v][i]:
                dfs(i)


visited = []
n, m = 7, 8
numbers = list(map(int,'1213242546566737'))
board = [[0]*(n + 1) for _ in range(n + 1)]
for i in range(0, len(numbers), 2):
    board[numbers[i]][numbers[i + 1]] = 1
    board[numbers[i + 1]][numbers[i]] = 1
dfs(1)
print(visited)
import sys
sys.stdin = open('input.txt')
from collections import deque

def dfs(v):
    print(v, end = ' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visit[v] = 0
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())
s = [[0] * (n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y], s[y][x] = 1, 1
print(s)
dfs(v)
print()
bfs(v)

for tc in range(1, 11):
    N = int(input())
    arr = []
    for i in range(1, 101):
        a.append(list(map(int, input().split())))
    print(arr)

    arr[][]
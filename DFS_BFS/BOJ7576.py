import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v):
    queue = deque([v])
    time[v] = 0
    cnt = 0
    while queue:
        v = queue.popleft()
        if



        queue.append(i)
        visit[i] = 0



if __name__ == "__main__":
    m, n = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(n)]
    start = []
    for i in range(n):
        for j in range(m):
            if boxes[i][j] == 1:
                start.append((i,j))
    print(start)
    visit = [[0]*6 for i in range(m*n+1)]

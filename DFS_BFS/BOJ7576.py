import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(v):
    queue = deque([v])
    visit[v] = 0
    while queue:
        v = queue.popleft()
        print(v, end = '')
        for visit[i] == 1 and s[v][i] == 1:
            queue.append(i)
            visit[i] = 0



if __name__ == "__main__":
    m, n = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(n)]
    visit = [0 for i in range(m*n+1)]

import time
import sys
sys.stdin = open('input.txt','r')

start = time.time()
from collections import deque
def bfs(v):
    queue = deque([v])
    visit[v] = 0
    while queue:
        v = queue.popleft()
        if v == K:
            print(visit[v])
        for i in (v-1, v+1, v*2):
            if 0 <= i < 10**5+1 and visit[i] == 0:
                queue.append(i)
                visit[i] = visit[v] + 1


if __name__ == '__main__':
    N, K = map(int, input().split())
    visit = [0]*(10**5+1)
    bfs(N)
    print(time.time() - start)
import sys
sys.stdin = open('input.txt')
from collections import deque
def bfs(v):
    global idx
    queue = deque([v])
    time[v] = 0
    cnt = 0
    while queue:
        v = queue.popleft()
        if v == K:
            idx = v
            cnt += 1
        for i in (v-1, v+1, v*2):
            if 0 <= i < 10**5+1 and time[i] >= time[v] + 1:
                if i == 2*v:
                    time[i] = time[v]
                else:
                    time[i] = time[v] + 1
                queue.append(i)
    print(time[K])

if __name__ == '__main__':
    N, K = map(int, input().split())
    idx = 0
    time = [float('inf')] * (10 ** 5 + 1)
    bfs(N)
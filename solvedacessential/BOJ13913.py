import sys
sys.stdin = open('input.txt','r')

from collections import deque
def bfs(v):
    queue = deque([v])
    visit[v] = [v]
    while queue:
        print(visit)
        v = queue.popleft()
        if v == K:
            print(len(visit[i]))
            print(' '.join(map(str, visit[i])))
            return
        for i in (v-1, v+1, v*2):
            if 0 <= i < 10**5+1 and visit[i] == 0:
                queue.append(i)
                visit[i] = visit[v] + [i]

if __name__ == '__main__':
    N, K = map(int, input().split())
    visit = [0]*(10**5+1)
    if N >= K:
        print(N - K)
        print(' '.join(map(str, list(range(N,K-1,-1)))))
    else:
        bfs(N)
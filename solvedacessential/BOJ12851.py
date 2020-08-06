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
                queue.append(i)
                time[i] = time[v] + 1
    print('%d\n%d'%(time[idx], cnt))


if __name__ == '__main__':
    N, K = map(int, input().split())
    if N >= K:
        print(N - K)
        print(1)
    else:
        idx = 0
        time = [float('inf')] * (10 ** 5 + 1)
        bfs(N)



'''
from collections import deque
def bfs(v):
    queue = deque([v])
    visit[v] = 0
    while queue:
        v = queue.popleft()
        if v == K:
            print(visit[v])
            return
        for i in (v-1, v+1, v*2):
            if visit[i] == K:
                print(visit[v])
            if 0 <= i < 10**5+1 and visit[i] == 0:
                queue.append(i)
                visit[i] = visit[v] + 1


if __name__ == '__main__':
    N, K = map(int, input().split())
    visit = [0]*(10**5+1)
    bfs(N)

#5 - 10 - 9 - 18 - 17
#5 - 4 - 8 - 16 - 17
'''
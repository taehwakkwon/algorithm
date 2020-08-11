import sys
sys.stdin = open('input.txt','r')


import sys
sys.setrecursionlimit(10**6)

from collections import deque
def bfs(v):
    queue = deque([v])
    visit[v] = 0
    while queue:
        print(queue)
        print(visit[:50])
        v = queue.popleft()
        if v == K:
            print(visit[v])
            return
        for i in (v-1, v+1, v*2):
            if 0 <= i < 10**5+1 and visit[i] == 0:
                queue.append(i)
                visit[i] = visit[v] + 1


if __name__ == '__main__':
    N, K = map(int, input().split())
    visit = [0]*(10**5+1)
    bfs(N)

'''
def c(n,k):
    if n>=k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return 1+min(c(n,k-1),c(n,k+1))
    else:
        return min(k-n, 1+c(n,k//2))
    
n, k = map(int,input().split())
print(c(n,k))
'''
import sys
sys.stdin = open('input.txt','r')

from collections import deque
def bfs(v):
    queue = deque([v])
    visit[v] = 0

    while queue:
        v = queue.popleft()
        for i in (v-1, v+1, v*2):
            if 0 <= i < 10**5+1 and visit[i] == 0:
                queue.append(i)
                visit[i] = visit[v] + 1
                if i == K:
                    print(visit[i])
                    return


if __name__ == '__main__':
    N, K = map(int, input().split())
    visit = [0]*(10**5+1)
    if N >= K:
        print(N - K)
    else:
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
=======
    if N >= K:
        print(N - K)
    else:
        bfs(N)
>>>>>>> 33da9fd9c7f6f90040c922ff00c3fbb487d2d25d

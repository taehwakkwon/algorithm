import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split()) #w, h
c, r = map(int, input().split()) # 4, 1
r = M - r

t = int(input())
visited = [[0]*(N+1) for _ in range(M+1)]

dr = [-1,-1,1,-1]
dc = [1,-1,-1,-1]
d = 0
num = 0
while num <= t:
    if 0 <= r <= M and 0 <= c <= N:
        visited[r][c] = num
        if num == t:
            print(c, M - r)
        num += 1
    else:
        r -= dr[d]
        c -= dc[d]
        d = (d + 1) % 4

    r += dr[d]
    c += dc[d]

for r in visited:
    print(*r)



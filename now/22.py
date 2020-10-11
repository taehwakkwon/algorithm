import sys
sys.stdin = open('input.txt')


M, N = map(int, input().split())
uni = []
total = []
for i in range(M):
    li = [[b, a] for a, b in enumerate(map(int, input().split()))]
    uni = sorted(li)
    for x in range(M-1):
        for y in range(x+1, M):
            if uni[x][0] == uni[y][0]:
                uni[x][1] = uni[y][1]

    result = []
    for x in range(N):
        result.append(uni[x][1])
    total.append(result)

cnt = 0
for i in range(M-1):
    for j in range(i+1,M):
        if total[i] == total[j]:
            cnt += 1

print(cnt)
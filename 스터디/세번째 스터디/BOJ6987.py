import sys
sys.stdin = open('input.txt')
#무승부: 짝수개
import time
import sys
sys.setrecursionlimit(10**7)
start = time.time()
def dfs(v, s):
    if sum(res) > 30:
        return
    if s == 15 and sum(res) == 30 and ' '.join(map(str, res[:])) not in result:
        result.add(' '.join(map(str, res[:])))
        print(len(result))
        return
    if v >= n:
        dfs(0, s)
        return
    else:
        for i in range(3):
            res[v * 3 + i] += 1
            for j in range(6):
                if v == j or visited[v][j] == 1 or visited[j][v] == 1:
                    continue
                res[j * 3 + 2 - i] += 1
                visited[v][j] = 1
                visited[j][v] = 1
                dfs(v + 1, s + 1)
                visited[v][j] = 0
                visited[j][v] = 0
                res[j * 3 + 2 - i] -= 1
            res[v*3 + i] -= 1


n = 6
res = [0]*3*n
result = set([])
visited = [[0]*n for _ in range(n)]
ans = []

a = input()
b = input()
c = input()
d = input()

dfs(0,0)
print(result)
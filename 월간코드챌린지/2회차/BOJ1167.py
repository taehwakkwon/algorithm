import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def dfs(node, s, exclude):
    global M
    if node > v:
        M = max(M, s)
        return
    else:
        if node in dic:
            for value in dic[node]:
                if dis[value[0]] == float('inf') and value[0] != exclude:
                    dis[value[0]] = value[1] + s
                    dfs(value[0], dis[value[0]], exclude)

v = int(input())
dic = {i:[] for i in range(1, v + 1)}
flag = False
for i in range(v-1):
    a, b, c = map(int, input().split())
    dic[a].append((b,c))
    dic[b].append((a,c))

dis = [0] + [float('inf')] * v
dis[1] = 0
dfs(1, 0, 0)
M = max(dis)
a = dis.index(M)
node = dis.index(M)
dis = [0] + [float('inf')] * v
dis[node] = 0
dfs(node, 0, 0)
M = max(dis)
b = dis.index(M)
dis = [0] + [float('inf')] * v
dis[a] = 0
dis[b] = 0
dfs(b,0, a)
m1 = max(dis)
dis = [0] + [float('inf')] * v
dis[a] = 0
dis[b] = 0
dfs(a,0,b)
m2 = max(dis)
print(max(m1,m2))
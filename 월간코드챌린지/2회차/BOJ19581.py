import sys
sys.stdin = open('input.txt')

def dfs(node, s):
    global M
    if node > v:
        M = max(M, s)
        return
    else:
        if node in dic:
            for value in dic[node]:
                if dis[value[0]] == float('inf'):
                    dis[value[0]] = value[1] + s
                    dfs(value[0], dis[value[0]])

v = int(input())
dic = {i:[] for i in range(1, v + 1)}
flag = False
for i in range(v-1):
    a, b, c = map(int, input().split())
    dic[a].append((b,c))
    dic[b].append((a,c))

dis = [0] + [float('inf')] * v
dis[1] = 0
dfs(1, 0)
M = max(dis)
if dis.count(M) > 1:
    flag = True
node = dis.index(M)
for i in range(1,v+1):
    dis[i] = float('inf')
dis[node] = 0
dfs(node, 0)
a = b = 0
M = max(dis)
dis[dis.index(M)] = 0
print(max(dis))
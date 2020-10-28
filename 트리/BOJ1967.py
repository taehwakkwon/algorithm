import sys
sys.stdin = open('input.txt')

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def find_deepest(v,s):
    global farest, loc
    if farest < s:
        farest = s
        loc = v
    if v in tree:
        for node, weight in tree[v]:
            if visited[node]:
                visited[node] = False
                find_deepest(node, s+weight)

n = int(input())
tree = defaultdict(list)
for i in range(n-1):
    a, b, c = map(int, input().split())
    #print(a,b,c)
    tree[a].append((b,c))
    tree[b].append((a,c))
farest = loc = 0
visited = [True]*(n+1)
find_deepest(1,0)
next_node = loc
farest = loc = 0
visited = [True]*(n+1)
find_deepest(next_node,0)
print(farest)
# print(tree)
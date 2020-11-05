import sys
sys.stdin = open('input.txt')

def find(x):
    if x == parent[x] : return x
    else: return find(parent[x])

def union(x,y):
    parent[find(y)] = find(x)

def kruskal(graph):
    mst = []
    graph = sorted(graph)
    mst_cost = 0
    while len(mst) < v:
        w, n1, n2 = graph.pop(0)
        if find(n1) != find(n2):
            union(n1, n2)
            mst.append((n1,n2))
            mst_cost += w
    return mst_cost



T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    graph = []
    parent = list(range(v+1))

    for i in range(e):
        n1, n2, w = map(int, input().split())
        graph.append((w,n1,n2))
    parent = list(range(v+1))

    print('#%d %d' %(t, kruskal(graph)))
    print(parent)






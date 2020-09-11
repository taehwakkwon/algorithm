import sys
sys.stdin = open('input.txt')


#정점이 트리에 들어있는곳 확인
#서브트리 카운트

def dfs(s, node, path):
    global flag
    if s > v or s == 0:
        return
    if s == node:
        flag = True
        path.append(s)
    elif not flag:
        dfs(tree[s][0], node, path)
        dfs(tree[s][1], node, path)
        if flag:
            path.append(s)

def count(node):
    global cnt
    if node == 0 or node > v:
        return
    cnt += 1
    count(tree[node][0])
    count(tree[node][1])


T = int(input())
for t in range(1, T + 1):
    v, e, node1, node2 = map(int, input().split())
    tree = [[0]*2 for _ in range(v + 1)] #왼, 오, 부

    li = list(map(int, input().split()))
    for i in range(0,e*2,2):
        if tree[li[i]][0] == 0:
            tree[li[i]][0] = li[i + 1]
        else:
            tree[li[i]][1] = li[i + 1]
    flag = False
    path1 = []
    dfs(1, node1, path1)
    flag = False
    path2 = []
    dfs(1, node2, path2)
    for i in range(-1, -min(len(path1), len(path2)) - 1, -1):
        if path1[i] != path2[i]:
            break
    mutal_node = i + 1
    cnt = 0
    count(path1[mutal_node])

    print('#%d %d %d' %(t, path1[mutal_node], cnt))

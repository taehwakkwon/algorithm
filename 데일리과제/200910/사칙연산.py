import sys
sys.stdin = open('input.txt')

def cal(v):
    if type(tree[v][0]) == str:
        cal(tree[v][1])
        cal(tree[v][2])
        if tree[v][0] == '+':
            tree[v][0] = tree[tree[v][1]][0] + tree[tree[v][2]][0]
        if tree[v][0] == '-':
            tree[v][0] = tree[tree[v][1]][0] - tree[tree[v][2]][0]
        if tree[v][0] == '*':
            tree[v][0] = tree[tree[v][1]][0] * tree[tree[v][2]][0]
        if tree[v][0] == '/':
            tree[v][0] = tree[tree[v][1]][0] / tree[tree[v][2]][0]


T = 10
for t in range(1,T + 1):
    n = int(input())
    tree = [[-1]*3 for _ in range(n + 1)]
    for i in range(n):
        inputs = list(input().split())
        if len(inputs) > 2:
            tree[int(inputs[0])][0] = inputs[1]
            tree[int(inputs[0])][1] = int(inputs[2])
            tree[int(inputs[0])][2] = int(inputs[3])
        else:
            tree[int(inputs[0])][0] = int(inputs[1])
    cal(1)
    print('#%d %d'%(t, int(tree[1][0])))


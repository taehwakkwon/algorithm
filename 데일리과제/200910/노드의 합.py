import sys
sys.stdin = open('input.txt')


def sum(v):
    if v > n:
        return
    else:
        sum(2*v)
        sum(2*v+1)
        tree[v//2] += tree[v]

T = int(input())
for t in range(1, T + 1):
    n, m, l = map(int, input().split())
    tree = [0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        tree[a] = b
    sum(1)
    print('#%d %d' %(t,tree[l]))

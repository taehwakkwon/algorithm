import sys
sys.stdin = open('input.txt')


def dfs(v):
    global cnt
    if v == delete:
        return
    if v > n:
        cnt += 1
        return
    else:
        dfs(v*2)
        dfs(v*2+1)



n = int(input())
tree = [0] + list(map(int, input().split()))
for i in range(1,n+1):
    tree[i] += 1
print(tree)
delete = int(input())
cnt = 0
dfs(1)
print(cnt)
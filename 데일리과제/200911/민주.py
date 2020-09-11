import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    v, e, p, c = map(int,input().split())
    left = [0] * (v + 1)
    right = [0] * (v + 1)
    parents = [0]* (v + 1)
    node = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        a,b = node[i], node[i+1]
        if left[a] != 0:
            right[a] = b
        else:
            left[a] = b
        parents[b] = a
    print(right)
    print(left)
    print(p)
    if p in left:
        start1 = left.index(p)
    if p in right:
        start1 = right.index(p)

    if c in left:
        start2 = left.index(c)
    if c in right:
        start2 = right.index(c)

    path1, path2 = [start1], [start2]
    for i in range(v + 1):
        if parents[path1[-1]] != 0:
            path1.append(parents[path1[-1]])
        if parents[path2[-1]] != 0:
            path2.append(parents[path2[-1]])
    l = min(len(path1), len(path2))
    cnt = -1
    for i, j in zip(path1[::-1][:l],path2[::-1][:l]):
        if i != j:
            break
        cnt += 1
    print(cnt, path2,path1)
    break
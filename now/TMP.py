import sys
sys.stdin=open('../input.txt')
import time
start = time.time()

def push(li):
    global count
    count += 1
    idx = 1
    while li[0] > tree[idx][1]:
        idx = tree[idx][3]
    else:
        if tree[idx][3] == 0:
            tree[idx][3] = count
            tree[count][:2] = li
        else:
            if tree[idx][1] < li[0] < tree[tree[idx][3]][0]:
                tree[count][3] = tree[idx][3]
                tree[idx][3] = count
                tree[count][:2] = li
            else:
                tree[idx][2] = count
                tree[count][:2] = li
        return
    while li[1] < tree[idx][0]:
        idx = tree[idx][2]
    else:
        if tree[idx][2] == 0:
            tree[idx][2] = count
            tree[count][:2] = li
        else:
            if tree[idx][0] > li[0] > tree[tree[idx][3]][1]:
                tree[count][2] = tree[idx][2]
                tree[idx][2] = count
                tree[count][:2] = li
            else:
                tree[idx][3] = count
                tree[count][:2] = li
    return

count = 0
n = int(input())
M = 0
tree = [[float('inf'),0,0,0] for _ in range(n + 1)]
for i in range(n):
    pivot = n // 2
    a, b = map(int, input().split())
    push([a,b])
print(tree)




print(time.time()-start)
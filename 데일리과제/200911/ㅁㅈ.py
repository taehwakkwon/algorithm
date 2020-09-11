import sys
sys.stdin = open('input.txt')

def in_order(idx):
    global cnt
    if idx > v:
        return
    if idx != 0:
        cnt += 1
        in_order(left[idx])
        in_order(right[idx])

t = int(input())
for tc in range(1, t+1):
    v, e, p, c = map(int,input().split())
    left = [0 for _ in range(v+2)]
    right = [0 for _ in range(v+2)]
    bu = [0]*(v+2)
    node = list(map(int, input().split()))
    # print(left)
    # print(right)
    for i in range(0, e*2, 2):
        parent = node[i]
        child = node[i+1]
        bu[child] = parent
        # print(parent)
        # print(child)
        if left[parent] != 0:
            right[parent] = child
        else:
            left[parent] = child
    # 8, 3
    jo_1 = [bu[p]]
    for i in range(len(bu)):
        if bu[jo_1[-1]] != 0:
            jo_1.append(bu[jo_1[-1]])

    jo_2 = [bu[c]]
    for i in range(len(bu)):
        if bu[jo_2[-1]] != 0:
            jo_2.append(bu[jo_2[-1]])

    s = 1
    for i in range(min(len(jo_1), len(jo_2))):
        if jo_1[::-1][i] != jo_2[::-1][i]:
            s = bu[jo_1[::-1][i]]
            break
    cnt = 0
    in_order(s)
    print('#%d %d %d' %(tc, s ,cnt))
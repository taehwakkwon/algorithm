import sys
sys.stdin = open('input.txt')

import time
st = time.time()
def push(a, b):
    if not disjoint:
        disjoint.append(set([a,b]))
        return len(disjoint[0])
    else:
        dic = {a:-1, b:-1}
        for i in range(len(disjoint)):
            if a in disjoint[i]:
                dic[a] = i
            if b in disjoint[i]:
                dic[b] = i
        if dic[a] >= 0 and dic[b] >= 0:
            if dic[a] == dic[b]:
                pass
            elif dic[a] > dic[b]:
                left = disjoint.pop(dic[a])
                disjoint[dic[b]] = disjoint[dic[b]] | left
            else:
                left = disjoint.pop(dic[a])
                disjoint[dic[a]] = disjoint[dic[a]]|left
        elif dic[a] >= 0:
            disjoint[dic[a]].add(b)
        elif dic[b] >= 0:
            disjoint[dic[b]].add(a)
        else:
            disjoint.append(set([a,b]))
        M = 0
        for i in range(len(disjoint)):
            M = max(M, len(disjoint[i]))
        return M


T = int(input())
for t in range(1, T+1):
    n = int(input())
    disjoint = []
    names = set([])
    for i in range(n):
        a, b = input().split()
        print(push(a,b))
        names.add(a)
        names.add(b)
print(time.time()-st)


import time
import sys
sys.setrecursionlimit(10**7)

def check(y,x):
    if not ch:
        return True
    else:
        for i in range(len(ch)):
            if y == ch[i][0] or x== ch[i][1] or abs(y-ch[i][0]) == abs(x-ch[i][1]):
                return False
        return True


def dfs(s,y,x):
    global cnt
    if s == N:
        tmp = sorted(ch)
        if tmp not in res:
            res.append(tmp)
    else:
        i, j = y, x
        while i < N:
            if i in row:
                i += 1
                continue
            while j < N:
                if j in col:
                    j += 1
                    continue
                if check(i,j):
                    ch.append((i,j))
                    row.append(i)
                    col.append(j)
                    dfs(s + 1, i + 1, 0)
                    ch.remove((i,j))
                    row.remove(i)
                    col.remove(j)
                j += 1
            i += 1
for i in range(16):
start = time.time()
res = []
cnt = 0
N = i
ch = []
row = []
col = []
dfs(0,0,0)
    print('#%d %d' %(i, len(res)))
    print('time:',time.time()-start)
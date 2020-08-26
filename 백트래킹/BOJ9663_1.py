import time
import sys
sys.setrecursionlimit(10 ** 7)

def dfs(s):
    global cnt, y, x
    if s == N:
        cnt += 1
    else:
        i, j = y, x
        while i < N:
            if i in col:
                i += 1
                continue
            while j < N:
                if j in ch:
                    j += 1
                    continue
                for p, q in ch.items():
                    if abs(i - q) == abs(j - p):
                        break
                else:
                    col[i] = 0
                    ch[j] = i
                    y, x = i + 1, 0
                    dfs(s + 1)
                    del col[i]
                    del ch[j]
                j += 1
            i += 1

cnt = 0
N = int(input())
ch = {}
col = {}
y, x = 0, 0
dfs(0)
print(cnt)
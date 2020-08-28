#import sys
#sys.stdin = open('sample_input.txt')
def dfs(v):
    global res
    if v == g:
        res = 1
    else:
        for i in range(51):
            if board[v][i]:
                board[v][i] = 0
                dfs(i)

#```python

#```
T = int(input())
for tc in range(1, 1 + T):
    res = 0
    v, e = map(int, input().split())
    board = [[0]*(51) for _ in range(51)]
    for i in range(e):
        s, g = map(int,input().split())
        board[s][g] = 1
    s, g = map(int, input().split())
    dfs(s)
    print('#%d %d' %(tc, res))

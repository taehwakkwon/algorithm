import sys
sys.stdin = open('input.txt')
#A-F, B-D, C-E

import sys
sys.setrecursionlimit(10**7)
def dfs(v, p, s):
    global M
    if v == n:
        if M < s:
            M = s
        return
    else:
        m = 0
        for i in range(6):
            if dice[v][i] != p and i != order[dice[v].index(p)]:
                if m < dice[v][i]:
                    m = dice[v][i]
        dfs(v + 1, dice[v][order[dice[v].index(p)]], s + m)


order = {0:5,1:3,2:4,3:1,4:2,5:0}
M = 0
ch = [1]*6
n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
for i in range(1,7):
    dfs(0,i,0)
print(M)

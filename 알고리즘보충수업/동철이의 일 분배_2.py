import sys
sys.stdin = open('input.txt')

from itertools import permutations
#순열의 갯수가 12개가 넘어가면 속도문제 발생
#속도를 올릴 수 있는 방법 고민

def dfs(v, p, l):
    global M
    if M > p:
        return
    if v == n:
        if M < p:
            M = p
    else:
        for i in range(n):
            ch[v][l*10+i]
            dfs(v + 1, board[v][i]*p/100,)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    M = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    comb = list(permutations())

    print('#%d %.6f' %(t, round(M*100,7)))
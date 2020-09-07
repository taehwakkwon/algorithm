import sys
sys.stdin = open('input.txt')

#순열의 갯수가 12개가 넘어가면 속도문제 발생
#속도를 올릴 수 있는 방법 고민

def dfs(v, p):
    global M
    if M >= p:
        return
    if v == n:
        M = max(M, p)
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                dfs(v + 1, board[v][i]*p/100)
                ch[i] = 0



T = int(input())
for t in range(1, T + 1):
    n = int(input())
    M = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    ch = [0]*n
    dfs(0, 1)
    print('#%d %.6f' %(t, 100*M))
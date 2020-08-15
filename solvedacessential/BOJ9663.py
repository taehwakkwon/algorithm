import sys
sys.stdin = open('input.txt')
def check(x,y):
    for i, j in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
        k, l = x, y
        while 0 <= k < n and 0 <= l < n:
            if board[k][l] == 0:
                k += i
                l += j
                continue
            else:
                return False
    return True

def dfs(x,y,q):
    global cnt
    if check(x,y) == False:
        return
    if q == n:
        cnt += 1
    else:
        dfs(x)


n = int(input())
if n < 3:
    print(0)
    sys.exit()
board = [[0]*n for _ in range(n)]
cnt = 0
dfs(0,0,0,0)
print(board)
print(cnt)



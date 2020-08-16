import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(100000)
def dfs(y,x):
    board[y][x] = 0
    for dy,dx in [(0,1),(-1,0),(0,-1),(1,0)]:
        if 0 <= y + dy < m and 0 <= x + dx < n and board[y + dy][x + dx] == 1:
            #board[y + dy][x + dx] = 0
            dfs(y + dy, x + dx)


if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        m,n,k = map(int, input().split())
        board = [[0]*n for _ in range(m)]
        cnt = 0
        for l in range(k):
            y,x = map(int, input().split())
            board[y][x] = 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    cnt += 1
                    dfs(i,j)
        res.append(cnt)
    for r in res:
        print(r)




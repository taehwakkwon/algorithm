import sys
sys.stdin = open('input.txt')

import sys
def go():
    count = [0]*n
    for i in range(n):
        now = i
        for j in range(h):
            if board[j][i] != 0:
                if 0 <= now - 1 < n and board[j][now-1] == board[j][now]:
                    now = now-1
                elif 0 <= now + 1 < n and board[j][now+1] == board[j][now]:
                    now = now+1
        if now != i:
            return False
        count[now] = 1
    return True

def dfs(r,c,s):



    if go():
        print(s)
        sys.exit()
    if s > 3 or r == h:
        return
    if c == n - 1:
        dfs(r + 1, 0, s)
    else:
        print(r, c, s)
        for pp in board:
            print(pp)
        print()
        if board[r][c] == board[r][c + 1] == 0:
            board[r][c] = board[r][c + 1] = s + 2
            dfs(r, c + 1, s + 1)
            board[r][c] = board[r][c + 1] = 0
        dfs(r, c + 1, s)



if __name__ == "__main__":
    n, m, h = map(int, input().split())
    MAX_BRIDGE = n*h

    board = [[0]*n for _ in range(h)]

    for i in range(m):
        a, b = map(int ,input().split())
        board[a-1][b-1] = board[a-1][b] = 1
    for pp in board:
        print(pp)
    print()
    dfs(0,0,0)
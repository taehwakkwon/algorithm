import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    board[0][0] = 1
    r, c, idx = 0, 0, 0
    for i in range(2, n**2+1):
        if 0 <= r + dr[idx] < n and 0 <= c + dc[idx]  < n and board[r + dr[idx]][c + dc[idx]] == 0:
            r += dr[idx]
            c += dc[idx]
            board[r][c] = i
        else:
            idx += 1
            idx %= 4
            r += dr[idx]
            c += dc[idx]
            board[r][c] = i
    print('#%d' %t)
    for r in board:
        print(' '.join(map(str,r)))

#총 3문제, 알고리즘

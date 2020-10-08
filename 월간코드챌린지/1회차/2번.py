import sys
def solution(n):
    board = []
    total =0
    for i in range(1, n+1):
        board.append([0]*i)
        total += i

    snail = 1
    r,c = 0,0
    board[r][c] = 1
    l = n
    while total > snail:
        for dr, dc in [(1,0),(0,1),(-1,-1)]:
            for i in range(l - 1):
                if 0 <= r < n and 0 <= c < n and board[r + dr][c + dc] == 0:
                    r += dr
                    c += dc
                    snail += 1
                    board[r][c] = snail
        l -= 2
    ans = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            ans.append(board[i][j])
    return ans



print(solution(4))
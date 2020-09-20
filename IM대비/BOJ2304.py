import sys
sys.stdin = open('input.txt')

n = int(input())
board = [0]*1001
for i in range(n):
    a, b = map(int,input().split())
    board[a] = b
M = max(board)
idx = board.index(M)
for i in range(idx):
    for j in range(i, idx):
        if board[i] < board[j]:
            break
        board[j] = board[i]
for i in range(1000,idx,-1):
    for j in range(i, idx, -1):
        if board[i] < board[j]:
            break
        board[j] = board[i]
print(sum(board))

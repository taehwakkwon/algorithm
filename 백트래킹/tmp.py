import sys
sys.stdin = open('input.txt')
import time
start = time.time()
import sys

cnt = 0
board = []
for i in range(5):
    tmp = []
    for j in range(5):
        tmp.append(cnt)
        cnt += 1
    board.append(tmp)
for r in board:
    print(*r)
print()
for i in range(5):
    for j in range(i + 1):
        print(board[5 - i - 1 + j][j], end = ' ')
    print()

for i in range(5):
    for j in range(i + 1):
        print(board[i - j][5 - j - 1], end = ' ')
    print()


print(time.time() - start)
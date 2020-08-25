import sys
sys.stdin = open('sample_input.txt')
import time
start = time.time()


def transpose():
    for i in range(100):
        for j in range(i + 1, 100):
            board[i][j], board[j][i] = board[j][i], board[i][j]


def solve():
    global M
    for i in range(100):
        for j in range(100, 2, -1):
            for k in range(100 - j + 1):
                if board[i][k:k + j] == board[i][k:k + j][::-1]:
                    if M < j:
                        M = j
                        break


T = 10

for t in range(1, T + 1):
    M = 0
    n = int(input())
    board = [list(input()) for _ in range(100)]
    solve()
    transpose()
    solve()
    print('#%d %d' % (t, M))
print(time.time()-start)
import sys
sys.stdin = open('sample_input.txt')
import time
start = time.time()
def transpose():
    new_board = []
    tmp = []
    for i in range(100):
        tmp.append(list(board[i]))
    for i in range(100):
        for j in range(i, 100):
            tmp[i][j], tmp[j][i] = tmp[j][i], tmp[i][j]
    for i in range(100):
        new_board.append(''.join(tmp[i]))
    return new_board


def solve(i):
    global M
    for j in range(100,2,-1):
        for k in range(100 - j + 1):
            if board[i][k:k+j] == board[i][k:k+j][::-1]:
                if M < j:
                    M = j
                    return


T = 10

for t in range(1, T + 1):
    M = 0
    n = int(input())
    board = [input() for _ in range(100)]
    for i in range(100):
        solve(i)
    new_board = transpose()
    for i in range(100):
        for j in range(i,100):
            if board[i][j] != new_board[j][i]:
                continue

    for i in range(100):
        solve(i)
    print('#%d %d' %(t, M))
print(time.time()-start)

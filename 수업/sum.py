import sys
import time
sys.stdin = open('input.txt')

start = time.time()
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def max(*args):
    M = args[0]
    for nu in args[1:]:
        if M < nu:
            M = nu
    return M

def max_list(number_list):
    M = number_list[0]
    for nu in number_list[1:]:
        if M < nu:
            M = nu
    return M

T = 10
for t in range(1, T + 1):
    n = int(input())
    board = [0]*100
    M = 0
    left = 0
    right = 99
    a, b = 0, 0
    for i in range(100):
        line = list(map(int, input().split()))
        a += line[left]
        b += line[right]
        left += 1
        right -= 1
        tmp = sum(line)
        if M < tmp:
            M = tmp
        for j in range(100):
            board[j] += line[j]
    print('#%d %d' %(n, max(a,b,M,max_list(board))))
print("time:", time.time() - start) #현재시각(코드 실행 후) - 시작시간(코드 실행 전)





'''
def find_max_c(board):
    M = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += board[j][i]
        if M < tmp:
            M = tmp
    return M



T = 10
for t in range(1, T + 1):
    n = int(input())
    board = []
    M = 0
    for i in range(100):
        line = list(map(int, input().split()))
        tmp = sum(line)
        if M < tmp:
            M = tmp
        board.append(line)
    M = max(M,find_max_c(board))
    a, b = 0, 0
    for i in range(len(board)):
        a += board[i][i]
        b += board[i][len(board)-1-i]
    print('#%d %d' %(n, max(a,b,M)))

'''
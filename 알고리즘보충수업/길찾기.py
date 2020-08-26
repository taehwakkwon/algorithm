import sys
sys.stdin = open('input.txt')

def dfs(v):
    global res
    if v == 99:
        res = 1
        return
    else:
        for i in range(100):
            if board[v][i]:
                board[v][i] = 0
                dfs(i)


T = 10
for t in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    board = [[0]*(100) for _ in range(100)]
    res = 0
    for i in range(0, len(numbers), 2):
        board[numbers[i]][numbers[i+1]] = 1
    dfs(0)
    print('#%d %d' %(t, res))
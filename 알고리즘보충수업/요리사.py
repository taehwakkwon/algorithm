import sys
sys.stdin = open('input.txt')


#두개로 나눠 -> 이중포문으로 다 더해
def combinations(v, s, res):
    if v == m:
        tmp = 0
        for i in range(m):
            for j in range(i):
                tmp += board[res[i]][res[j]]
        result.append(res[:])
    else:
        for i in range(s, n):
            res[v] = i
            combinations(v + 1, i + 1, res)

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i):
            board[i][j] += board[j][i]
            board[j][i] = 0
    m = n // 2
    result = []
    res = [0] * m
    combinations(0, 0, res)
    M = float('inf')
    #print(result[:n//2+1], result[n//2+1:][::-1])
    for left, right in zip(result[:n//2 + 1],result[n//2 + 1:][::-1]):
        a, b = 0, 0
        for i in range(len(left)):
            for j in range(i):
                a += board[left[i]][left[j]]
                b += board[right[i]][right[j]]
        M = min(M, abs(a-b))
    print('#%d %d' %(t,M))


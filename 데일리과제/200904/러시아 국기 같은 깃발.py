import sys
sys.stdin = open('input.txt')

def combinations(v, s, res):
    if v == 2:
        result.append(tuple(res))
    else:
        for i in range(s, n - 1):
            res[v] = i
            combinations(v + 1, i + 1, res)


def solve():
    global M
    for i, j in result:
        cnt = 0
        for k in range(i + 1):
            cnt += (m - flag[k].count('W'))
        for k in range(i + 1, j + 1):
            cnt += (m - flag[k].count('B'))
        for k in range(j + 1, n):
            cnt += (m - flag[k].count('R'))
        if cnt < M:
            M = cnt
    return M


T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    M = float('inf')
    result = []
    res = [0, 0]
    combinations(0,0,res)
    solve()
    print('#%d %d'M)

import sys
sys.stdin = open('input.txt')

def combinations(v, s, res):
    if v == 2:
        result.extend(res[:])
        return
    else:
        for i in range(s, n):
            combinations(v + 1, i + 1, res + [i])


def dfs(v):
    global res
    if v == 15:
        if sum(ans) == 0:
            res = 1
        return
    else:
        for i in range(3):
            if ans[result[v * 2] * 3 + i] and ans[result[v * 2 + 1] * 3 + 2 - i]:
                ans[result[v * 2] * 3 + i] -= 1  # 승
                ans[result[v * 2 + 1] * 3 + 2 - i] -= 1  # 패
                dfs(v + 1)
                ans[result[v * 2] * 3 + i] += 1  # 승
                ans[result[v * 2 + 1] * 3 + 2 - i] += 1  # 패

n = 6
result = []
combinations(0, 0, [])
for i in range(4):
    res = 0
    ans = list(map(int, input().split()))

    dfs(0)
    print(res, end = ' ')

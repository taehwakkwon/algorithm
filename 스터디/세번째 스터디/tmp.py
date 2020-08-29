import sys
sys.stdin = open('input.txt')
import sys
sys.setrecursionlimit(10**7)
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
        if ans[result[v * 2] * 3] and ans[result[v * 2 + 1] * 3 + 2]:
            ans[result[v * 2] * 3] -= 1 #승
            ans[result[v * 2 + 1] * 3 + 2] -= 1 #패
            dfs(v + 1)
            ans[result[v * 2] * 3] += 1  # 승
            ans[result[v * 2 + 1] * 3 + 2] += 1  # 패

        if ans[result[v * 2] * 3 + 1] and ans[result[v * 2 + 1] * 3 + 1]:
            ans[result[v * 2] * 3 + 1] -= 1  # 무
            ans[result[v * 2 + 1] * 3 + 1] -= 1  # 무
            dfs(v + 1)
            ans[result[v * 2] * 3 + 1] += 1  # 무
            ans[result[v * 2 + 1] * 3 + 1] += 1  # 무

        if ans[result[v * 2] * 3 + 2] and ans[result[v * 2 + 1] * 3]:
            ans[result[v * 2] * 3 + 2] -= 1  # 패
            ans[result[v * 2 + 1] * 3] -= 1  # 승
            dfs(v + 1)
            ans[result[v * 2] * 3 + 2] += 1  # 패
            ans[result[v * 2 + 1] * 3] += 1  # 승


n = 6
result = []
combinations(0, 0, [])
for i in range(16):
    res = 0
    ans = list(map(int, input().split()))

    dfs(0)
    print(res, end = ' ')
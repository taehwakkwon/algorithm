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
    for i in range(15):
        if a[i] < ans[i]:
            return
    if v == 15:
        visited.add(str(ans))
        return
    else:
        ans[result[v * 2] * 3] += 1 #승
        ans[result[v * 2 + 1] * 3 + 2] += 1 #패
        dfs(v + 1)
        ans[result[v * 2] * 3] -= 1  # 승
        ans[result[v * 2 + 1] * 3 + 2] -= 1  # 패

        ans[result[v * 2] * 3 + 1] += 1  # 무
        ans[result[v * 2 + 1] * 3 + 1] += 1  # 무
        dfs(v + 1)
        ans[result[v * 2] * 3 + 1] -= 1  # 무
        ans[result[v * 2 + 1] * 3 + 1] -= 1  # 무

        ans[result[v * 2] * 3 + 2] += 1  # 패
        ans[result[v * 2 + 1] * 3] += 1  # 승
        dfs(v + 1)
        ans[result[v * 2] * 3 + 2] -= 1  # 패
        ans[result[v * 2 + 1] * 3] -= 1  # 승


n = 6
ans = [0]*n*3
result = []
combinations(0, 0, [])
visited = set([])
for i in range(4):
    res = 0
    a = list(map(int, input().split()))
    dfs(0)
    print(res)


    #dfs(list(map(int, input().split())), 30)
    #print(ans, end = ' ')

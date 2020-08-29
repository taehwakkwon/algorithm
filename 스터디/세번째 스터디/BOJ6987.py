import sys
sys.stdin = open('input.txt')
#무승부: 짝수개
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
for i in range(4):
    res = 0
    ans = list(map(int, input().split()))

    dfs(0)
    print(res, end = ' ')




# def dfs(v, s):
#
#     if sum(res) > 30:
#         return
#     if s == 15 and sum(res) == 30 and ' '.join(map(str, res[:])) not in result:
#         result.add(' '.join(map(str, res[:])))
#         print(len(result))
#         return
#     if v >= n:
#         dfs(0, s)
#         return
#     else:
#         for i in range(3):
#             res[v * 3 + i] += 1
#             for j in range(6):
#                 if v == j or visited[v][j] == 1 or visited[j][v] == 1:
#                     continue
#                 res[j * 3 + 2 - i] += 1
#                 visited[v][j] = 1
#                 visited[j][v] = 1
#                 dfs(v + 1, s + 1)
#                 visited[v][j] = 0
#                 visited[j][v] = 0
#                 res[j * 3 + 2 - i] -= 1
#             res[v*3 + i] -= 1
#         return

def combinations(v, s, res):
    if v == 2:
        result.append(res[:])

        return
    else:
        for i in range(s, n):
            combinations(v + 1, i + 1, res + [i])

# def record(v):
#     if v >= len(result):
#         print(*cnt)
#         return
#     else:
#         for i in range(len(result)):
#             for j in range(3):
#                 cnt[result[v][0] * 3 + j] += 1
#                 cnt[result[v][1] * 3 + 2 - j] += 1
#                 record(v + 1)
#                 cnt[result[v][0] * 3 + j] -= 1
#                 cnt[result[v][1] * 3 + 2 - j] -= 1
def record(numbers, s):
    global ans
    if s == 0:
        ans = 1
    else:
        for i in range(n):
            for j in range(3):
                if numbers[i * 3 + j] and str(numbers) not in visited:
                    visited.add(str(numbers))
                    numbers[i * 3 + j] -= 1
                    s -= 1
                    for k in range(n):
                        if i == k:
                            continue
                        if numbers[k * 3 + 2 - j]:
                            numbers[k * 3 + 2 - j] -= 1
                            record(numbers, s - 1)
                            numbers[k * 3 + 2 - j] += 1
                    s += 1
                    numbers[i * 3 + j] += 1

n = 6
for i in range(16):
    visited = set([])
    ans = 0
    record(list(map(int, input().split())), 30)
    print(ans, end = ' ')

#1 1 0 0 0 0 0 0 1 1 1 1 0 0 0 0
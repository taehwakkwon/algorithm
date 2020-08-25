import sys
sys.stdin = open('input.txt')
# def solve(v, sum, flag, res):
#     global cnt
#     if sum > s:
#         return
#     if sum == s and flag:
#         print(v, sum)
#         print(res)
#         result.add(' '.join(map(str, res)))
#         cnt += 1
#         return
#     if v >= n:
#         return
#     else:
#         solve(v + 1, sum, flag, res)
#         res.append(numbers[v])
#         solve(v + 1, sum + numbers[v], True, res)

def solve(v, sum):
    global cnt
    if v >= n:
        if sum == s:
            cnt += 1
            return
    else:
        solve(v + 1, sum + numbers[v])
        solve(v + 1, sum)

cnt = 0
n, s = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
solve(0,0)
if s:
    print(cnt)
else:
    print(cnt - 1)
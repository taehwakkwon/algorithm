import sys
sys.stdin = open('input.txt')

def solve(v, li,l):
    global cnt
    if v >= n:
        res.append(li[:])
    else:
        solve(v + 1, li + [numbers[v]])
        solve(v + 1, li)

cnt = 0
n, s = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
for i in range(1, n + 1):
    res = []
    solve(0,[])

solve(0,[])
print(res, len(res))
if s:
    print(cnt)
else:
    print(cnt - 1)

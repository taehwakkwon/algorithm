import sys
sys.stdin = open('input.txt')


import sys
sys.setrecursionlimit(10**7)
def sum(li):
    res = 0
    for i in range(len(li) - 1):
        res += abs(li[i] - li[i + 1])
    return res


def solve(li):
    global M
    if ' '.join(map(str,li)) in visited:
        return
    visited.add(' '.join(map(str,li)))
    s = sum(li)
    if M < s:
        M = s
    for i in range(n-1):
        solve(li[:i]+li[i:i+2][::-1] + li[i+2:])

visited = set([])
M = 0
n = int(input())
numbers = list(map(int, input().split()))
solve(numbers)
print(M)
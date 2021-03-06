import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**7)
def solve(v, sum, li, dic):
    if v >= len(li):
        dic[sum] = dic.get(sum,0) + 1
    else:
        solve(v + 1, sum + li[v], li, dic)
        solve(v + 1, sum, li, dic)

cnt = 0
n, s = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
left, right = numbers[:n//2], numbers[n//2:]
dic = {}
solve(0,0,left,dic)
l_dic = dic
dic = {}
solve(0,0,right,dic)
for key in l_dic:
    if s - key in dic:
        cnt += (l_dic[key] * dic[s-key])
if s == 0:
    cnt -= 1
print(cnt)
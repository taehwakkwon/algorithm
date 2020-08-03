import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())
dic = {}
for i in range(n):
    name = input()
    dic[name] = 1
for j in range(m):
    name = input()
    dic[name] = dic.get(name,0) - 1
res = []
for key, value in dic.items():
    if not value:
        res.append(key)
print(len(res))
for r in sorted(res):
    print(r)
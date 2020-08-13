import sys
sys.stdin = open('input.txt')

C, N = map(int,input().split())
# [[money, people], ... ]
info = [list(map(int,input().split())) for _ in range(N)]

for i in info:
    i.append(i[1]/i[0])
info.sort(key= lambda x :x[2],reverse=True)

cost = 0
tmp = 0
result = []
while C > 0 and tmp < N:
    cost += (C // info[tmp][1]) * info[tmp][0]
    C %= info[tmp][1]
    if C % info[tmp][1]:
        result.append(cost+info[tmp][0])
    else:
        result.append(cost)
        break
    tmp += 1
# print(result)
print(min(result))
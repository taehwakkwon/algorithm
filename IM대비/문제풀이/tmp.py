import sys
sys.stdin = open('../발표/창고다각형.txt')

n = int(input())
case = []
max_l = 0
max_h = 0
u = 0
for i in range(n):
    l,h = map(int,input().split())
    case.append([l,h])
    if l > max_l:
        max_l = l
    if h > max_h:
        max_h = h
        u = l
stick = [0] * (max_l+1)
for i in range(n):
    stick[case[i][0]] = case[i][1]

stick_sum = 0
h = 0
for i in range(len(stick)):
    if i > u:
        stick_sum += max(stick[u+1:max_l+1])
    elif i == u:
        stick_sum += max_h
    else:
        if stick[i] > h:
            h = stick[i]
        if stick[i] <= h:
            stick_sum += h
print(stick)
print(stick_sum)
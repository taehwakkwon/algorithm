import sys
sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline())
dic = []
for idx in range(T):
    S, E = map(int, (sys.stdin.readline()).split(' '))
    dic.append((S, E))

dic.sort(key=lambda x: (x[1],x[0]))
tmp = 0
cnt = 0
for idx in range(T):
    if tmp <= dic[idx][0]:
        cnt += 1
        tmp = dic[idx][1]
print(cnt)
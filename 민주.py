import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    li = list(map(int,input().split()))
    avg = sum(li[1:])/li[0]
    cnt = 0
    for j in range(1, len(li)):
        if li[j] > avg :
            cnt += 1
            a = (str("%.3f" %round((cnt/li[0])*100, 3))+"%")
    print(a)
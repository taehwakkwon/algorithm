import sys
sys.stdin = open('input.txt','r')
def dp(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 3
    pre = 1
    now = 3
    for i in range(2,n):
        pre = pre*2 + now
        pre,now = now, pre
    return now

while True:
    try:
        print(dp(int(input())))
    except:
        break
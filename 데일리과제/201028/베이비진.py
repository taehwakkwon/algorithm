import sys
sys.stdin = open('input.txt')
def check(li):
    cnt = 0
    for i in range(10):
        if i in li:
            cnt += 1
            if li.count(i) >= 3 or cnt >= 3:
                return True
        else:
            cnt = 0
    return False


T = int(input())
for t in range(1,T+1):
    cards = list(map(int, input().split()))
    a, b = [], []
    for idx in range(0,len(cards),2):
        a.append(cards[idx])
        if check(a):
            print('#%d %d' %(t, 1))
            break
        b.append(cards[idx+1])
        if check(b):
            print('#%d %d' % (t, 2))
            break
    else:
        print('#%d %d' % (t, 0))


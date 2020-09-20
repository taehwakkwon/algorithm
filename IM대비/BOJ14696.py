import sys
sys.stdin = open('input.txt')

#별 많
# 동
#네
#세

n = int(input())
for i in range(n):
    a = sorted(list(map(int, input().split()))[1:], reverse=True)
    b = sorted(list(map(int, input().split()))[1:], reverse=True)
    pivot = 0
    while len(a) > pivot and len(b) > pivot:
        if a[pivot] > b[pivot]:
            print('A')
            break
        elif a[pivot] < b[pivot]:
            print('B')
            break
        else:
            pivot += 1
    else:
        if len(a) > len(b):
            print('A')
        elif len(a) < len(b):
            print('B')
        else:
            print('D')

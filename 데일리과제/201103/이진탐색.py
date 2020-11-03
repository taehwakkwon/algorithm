import sys
sys.stdin = open('input.txt')

def BinarySearch(left, right, stack, num):
    global cnt
    mid = (left+right)//2
    if a[mid] == num:
        cnt += 1
    elif a[left] <= num < a[mid]:
        if stack == [] or stack[-1] != 'left':
            stack.append('left')
            BinarySearch(left, mid - 1,stack, num)
        else:
            return
    elif a[mid] < num <= a[right]:
        if stack == [] or stack[-1] != 'right':
            stack.append('right')
            BinarySearch(mid + 1, right, stack, num)
        else:
            return


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    cnt = 0
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    for num in b:
        BinarySearch(0,len(a)-1,[],num)
    print('#%d %d' %(t, cnt))


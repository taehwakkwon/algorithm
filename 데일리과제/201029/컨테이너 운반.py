import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    containers = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    idx = len(trucks) - 1
    cnt = 0

    while containers:
        right = containers.pop()
        if idx >= 0 and trucks[idx] >= right:
            cnt += right
            idx -= 1
    print('#%d %d' %(t,cnt))

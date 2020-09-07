import sys
sys.stdin = open('input.txt')



T = int(input())
for t in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    visited = set([0])
    cnt = 1


    print('#%d %d' %(t,s))
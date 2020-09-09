import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    visited = {0 : 0}
    for score in scores:
        for v in list(visited):
            visited[score + v] = 0
    print('#%d %d' %(t,len(visited)))
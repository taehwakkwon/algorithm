import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    stack = []
    arr = []
    m = float('inf')
    for n in range(N):
        arr.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                stack.append(arr[i][j])
                for p in range(N):
                    visited[p][j] = visited[i][p] = 1
                # for r in visited:
                #     print(*r)
                # print(arr[i][j], (i,j))
        print(stack)
        print(tc)

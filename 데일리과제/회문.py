import sys
sys.stdin = open('sample_input.txt')
def transpose(box):
    for i in range(N):
        for j in range(i + 1, N):
            box[i][j], box[j][i] = box[j][i], box[i][j]
    return box


def solve(N,M):
    for i in range(N):
        for j in range(N - M + 1):
            if box[i][j:j+M] == box[i][j:j+M][::-1]:
                print('#%d %s' %(t, ''.join(map(str,box[i][j:j+M]))))
                return box[i][j:j+M]
    transpose(box)
    solve(N, M)

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    box = [list(input()) for _ in range(N)]
    solve(N, M)
import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1,T+1):
    N = int(input())
    box_a = [[0]*N for _ in range(N)]
    ans = [['']*N for _ in range(N)]
    box_b = [[0]*N for _ in range(N)]
    box_c = [[0]*N for _ in range(N)]
    arr= [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    for r in range(N):
        for c in range(N):
            box_a[c][N-r-1] = arr[r][c]
            box_b[N-1-r][N-1-c] = arr[r][c]
            box_c[N - 1 - c][r] = arr[r][c]


    # print(box_a,box_b,box_c)
    print('#%d' % tc)
    for a, b, c in zip(box_a, box_b, box_c):
        print(''.join(map(str,a)),''.join(map(str,b)),''.join(map(str,c)))


import sys
sys.stdin = open('input.txt')

def dfs():


for i in range(1,100):
    N = i #작품 한변의 크기
    #K = int(input()) #창영이가 제거한 타일의 개수 K와 위치

    box = [[0] * N for _ in range(N)]
    arr = []
    new_c = 0
    for c in range(N//2+1):
        new_c = c % 3
        arr.append(new_c+1)

    for x in range(N//2 +1):
        num = arr.pop(0)
        for i in range(x, N-x):
            for j in range(x, N-x):
                box[i][j] = num

    for r in box:
        print(*r)
    print()
#
# for i in range(K):
#     a, b = map(int,input().split())
#     print(box[b-1][a-1])
import sys
sys.stdin = open('input.txt')

import copy

T = int(input())  # 테스트케이스 개수
for tc in range(1, T + 1):
    # N:배열의 크기, C:회전 각도, X,Y:시작위치, K:부분 영역의 가로 세로 값,R:출력 행
    N, C, X, Y, K, R = map(int, input().split())

    # 부분 사각형이 NXN 영역을 벗어나는 경우
    if X + K - 1 > N or Y + K - 1 > N:
        print('#%d' % tc, '-1')

    arr = [list(map(int, input().split())) for _ in range(N)]
    # 회전결과의 배열이 반영된 새 BOX
    K_box = copy.deepcopy(arr)

    # X,Y의 위치와 실제 사용되는 인덱스 값 일치 시키기위해 -1 계산
    i = Y - 1
    j = X - 1
    # 각도 계산해주기 (360도 이상의 값은 결국 90,180,270,360과 동일하기 때문에 나머지 연산)
    C = C % 360
    #C == 0일때

    # 각도가 90도 일 때
    if C == 90:
        # 부분 사각형 배열을 탐색하며
        for r in range(K):
            for c in range(K):
                # print(r,c)
                # print(arr[N - 1 - c + 1][r - 1])
                # 90도 회전 될 값을 새로운 box에 입력
                K_box[i+r][j+c]  = arr[i + c][j - r + K - 1]
                print(i+r, j + c, arr[i+r][j+c])
                print(i + c,j + K - 1 - r, arr[i+c][j+K-1-r])
                print()
    break
    #     # print(K_box)
    #     # 새 박스의 R행의 합 구하기
    #     for r in range(len(K_box)):
    #         for c in range(len(K_box[r])):
    #             sum(K_box[R - 1])
    #     print('#%d' % tc, sum(K_box[R - 1]))
    #
    # # 각도가 180도 일 때
    # elif C == 180:
    #     # 부분 사각형 배열을 탐색하며
    #     for r in range(i, i + K):
    #         for c in range(j, j + K):
    #             # print(arr[N - r + 1][N - c - 1])
    #             # 180도 회전 될 값을 새로운 box에 입력
    #             K_box[r][c] = arr[N - r + 1][N - c - 1]
    #     # 새 박스의 R행의 합 구하기
    #     for r in range(len(K_box)):
    #         for c in range(len(K_box[r])):
    #             sum(K_box[R - 1])
    #     print('#%d' % tc, sum(K_box[R - 1]))
    #
    # # 각도가 270도 일 때
    # elif C == 270:
    #     # 부분 사각형 배열을 탐색하며
    #     for r in range(i, i + K):
    #         for c in range(j, j + K):
    #             # print(arr[c+1][N - r])
    #             # 270도 회전 될 값을 새로운 box에 입력
    #             K_box[r][c] = arr[c + 1][N - r]
    #
    #     # 새 박스의 R행의 합 구하기
    #     for r in range(len(K_box)):
    #         for c in range(len(K_box[r])):
    #             sum(K_box[R - 1])
    #     print('#%d' % tc, sum(K_box[R - 1]))
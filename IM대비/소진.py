import sys
sys.stdin = open('input.txt')
C, R = map(int, input().split()) #C:행 #R:열
k = int(input()) #찾아야하는 좌석
Board = [[0]*C for _ in range(R)] #빈 공연장
total = R*C #좌석의 개수
num = 1 #좌석 번호
r = 0
c = 0
dir = 0
dr = [1, 0, -1, 0]  # 상우하좌
dc = [0, 1, 0, -1]
while num <= total:
    if 0 <= r < R and 0 <= c < C and Board[r][c] == 0:
        Board[r][c] = num
        if num == k:
            print(r+1,c+1)
        num += 1

    else: #범위를 벗어나면
        r -= dr[dir]
        c -= dc[dir]
        dir = (dir+1)%4
    r += dr[dir]
    c += dc[dir]


'''
3
3 3 3
1 2 3
4 5 6
7 8 9
4 4 3
2 3 4 3
5 6 7 8
9 7 9 7
1 2 4 5
6 5 4
11 75 97 9 36
14 33 72 12 57
44 77 38 98 67
38 30 69 16 48
45 29 35 64 56
23 75 48 87 45
'''
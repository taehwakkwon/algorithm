import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 전체 배열을 이차원 배열의 형태로 받음
    Board = [ list(map(int, input().split())) for _ in range(N) ]
    # visited = [ [0]*M for _ in range(N)]
    r = 0
    c = 0
    nr = 0
    nc = 0
    result = []
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    dir = 0
    #도넛의 시작점 구하기
    for r in range(N-K+1):
        for c in range(M-K+1):
            #한 도넛을 돌릴 때
            total = 0
            dir = 0
            cr,cc = r,c
            for i in range(K*K - (K-2)*(K-2)):
                total += Board[cr][cc]
                nr = cr + dr[dir]
                nc = cc + dc[dir]
                cr,cc = nr, nc

                if nr < r or nc < c or nr >= r+K or nc >= c+K:
                    nr -= dr[dir]
                    nc -= dc[dir]
                    cr, cc = nr, nc

                    dir = (dir+1) % 4
                    nr = cr + dr[dir]
                    nc = cc + dc[dir]
                    cr, cc = nr, nc


            result.append(total)
    print(tc, result)
    print(max(result)-min(result))

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
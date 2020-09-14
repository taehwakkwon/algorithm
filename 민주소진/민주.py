import sys
sys.stdin = open('input.txt')

#재귀깊이 1000
#최대 재귀깊이 2500
#런타임에러 -> 재귀깊이, 인덱스에러, while 탈출확인
import sys
sys.setrecursionlimit(100000)
def dfs(r, c):
    global ta, M, N
    dr = [0, 0, -1, 1] # 상하좌우
    dc = [-1, 1, 0, 0]
    ta[r][c] = 0 #방문 한 것을 확인하였으니 -1로 체크
    for q in range(4):
        cr, cc = r+dr[q], c+dc[q] #현재의 좌표
        if cc <= -1 or cc == N or cr == -1 or cr == M:
             continue
        if ta[cr][cc] == 1:
            ta[cr][cc] = 0
            dfs(cr, cc)


t = int(input())
for tc in range(1, t+1):
    M, N, K = map(int, input().split())
    ta = [[0]*N for _ in range(M)]
    cnt = 0
    for i in range(K):
        a, b = map(int, input().split())
        ta[a][b] = 1

    for r in range(M):
        for c in range(N):
            if ta[r][c] != 0:
                cnt += 1
                dfs(r, c)
    print(cnt)
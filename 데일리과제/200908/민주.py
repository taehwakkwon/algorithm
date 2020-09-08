import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = [(input().split()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            cnt = 1 # 경로의 길이를 처음 잴때
            cnt = dfs()
            if cnt > max_cnt:
                max_cnt = cnt
                start = li[i][j]
            elif cnt == max_cnt:
                if start > li[i][j]:
                    start = li[i][j]




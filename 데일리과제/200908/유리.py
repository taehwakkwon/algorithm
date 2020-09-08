import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split()))  for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    queue = []
    visited = [[0] * N for _ in range(N)]
    cnt = 1
    cnt_list = []
    for i in range(N):
        for j in range(N):
            start = room[i][j]
            visited[i][j] = 1
            r, c = i, j
            queue.append((r, c, cnt))
            while queue:
                cr, cc, count = queue.pop(0)
                for k in range(4):
                    nr = cr + dr[k]
                    nc = cc + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                        if room[cr][cc]+1 == room[nr][nc]:
                            queue.append((nr, nc, count+1))
                #max(count)
    #print(count)
            cnt_list.append((count, start))
    print(sorted(cnt_list, reverse = True))
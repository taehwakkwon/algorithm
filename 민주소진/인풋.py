def dfs():
    global cnt
    stack = []
    visited = [[0]*(M) for _ in range(N)]
    dr = [1, -1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            if pond[i][j] == 1 and visited[i][j] == 0:
                stack.append((i, j))
                cnt += 1
                # while pond[r][c] == 0:
                while stack:
                    cr, cc = stack.pop()
                    visited[cr][cc] = 1
                    for i in range(4):
                        cr += dr[i]
                        cc += dc[i]
                        if 0 <= cr < N and 0 <= cc < M and visited[cr][cc] == 0:
                            stack.append((cr,cc))
    return cnt

T = int(input())
for tc in range(1,T+1):
    M, N, K = map(int, input().split())
    pond = [[0]*M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        pond[y][x] = 1
    cnt = 0
    result = dfs()
    print(result)

    for p in pond:
        print(*p)
    print()
            # print(x, y)

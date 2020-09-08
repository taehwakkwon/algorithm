import sys
sys.stdin = open('input.txt')

def dfs():
    global arr,cnt,visited,max_cnt
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    visited = [[0] * N for _ in range(N)]
    stack = list()
    stack.append((i, j))
    while stack: #스택이 비어있지 않다면 == 스택에 시작점이 있다면
        cr, cc = stack.pop()
        visited[cr][cc] = 1
        for x in range(4):
            nr = cr + dr[x]
            nc = cc + dc[x]
            if 0 <= nr < len(arr) and  0 <=nc < len(arr) and arr[nr][nc] == arr[cr][cc] + 1 and not visited[nr][nc]:
                stack.append((nr,nc))
                cnt += 1
    return cnt
    # if max_cnt < cnt:
    #     max_cnt = cnt
    #     result = arr[cr][cc]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    result = 0
    start = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            cnt = dfs()
            if cnt > max_cnt:
                max_cnt = cnt
                start = arr[i][j]
            elif cnt == max_cnt:
                start = min(arr[i][j], start)

    print("#%d" %tc, start, max_cnt)
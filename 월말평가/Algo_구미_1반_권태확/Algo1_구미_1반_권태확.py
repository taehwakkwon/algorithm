move = [(0,1),(1,0),(0,-1),(-1,0)]
loc = [(0,0),(0,1),(1,1),(1,0)]
T = int(input())
for t in range(1, T+1):
    n, c, x, y, k, r = map(int, input().split())
    x -= 1
    y -= 1
    c %= 360 #360회전 == 0회전
    c //= 90 #90도 회전할 때마다 1씩 증가하는범위로 변경
    board = [list(map(int, input().split())) for _ in range(n)]
    new_board = [[0]*n for _ in range(n)]
    if x + k > n or y + k > n: #회전불가능
        ans = -1
    else:
        by, bx = y, x
        ny, nx = y + (k-1)*loc[c][0], x + (k-1)*loc[c][1] #시작점(?) 찾기
        new_board[ny][nx] = board[by][bx]
        for i in range(4):
            for j in range(k-1):
                ny,nx = ny + move[(i+c)%4][0], nx + move[(i+c)%4][1]
                by, bx = by + move[i][0], bx + move[i][1]
                new_board[ny][nx] = board[by][bx]
        for i in range(n):
            for j in range(n):
                if new_board[i][j] == 0:
                    new_board[i][j] = board[i][j] #new_board에 회전하지 않은 지점 값 삽입
        ans = sum(new_board[r-1])
    for rr in new_board:
        print(rr)
    print('#%d %d' %(t, ans))
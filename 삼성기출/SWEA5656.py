import sys
sys.stdin = open('../now/input.txt')
def boom(r,c,k):
    board[r][c] = 0
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr, nc = r, c
        for i in range(k-1):
            nr += dr
            nc += dc
            if 0 <= nr < h and 0 <= nc < w:
                if board[nr][nc] != 0:
                    boom(nr,nc, board[nr][nc])


def get_ordered():
    for i in range(w):
        for j in range(h-1,-1,-1):
            if board[j][i] == 0:
                for k in range(j-1, -1,-1):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
                        break
                else:
                    break
def product_permutation(v):
    if v >= n:
        result.append(tuple(res))
        return
    else:
        for i in range(w):
            res[v] = i
            product_permutation(v+1)

def copy():
    global m
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0:
                cnt += 1
            board[i][j] = copyed[i][j]
    return cnt



T = int(input())
for t in range(1,T+1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    total = 0
    m = float('inf')
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0:
                total += 1
    res = [0]*n
    result = []
    product_permutation(0)
    # boom(2,2,board[2][2])
    # get_ordered()
    copyed = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            copyed[i][j] = board[i][j]

    for per in result:
        for p in per:
            for j in range(h):
                if board[j][p] != 0:
                    boom(j,p,board[j][p])
                    get_ordered()
                    break
            else:
                break

        cnt = copy()
        m = min(cnt, m)
    print('#%d %d' %(t, m))
    # tops = [0]*w
    # for i in range(w):
    #     for j in range(h):
    #         if board[j][i] != 0:
    #             tops[i] = board[j][i]
    #             break
    # print(tops)


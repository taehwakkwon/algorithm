

def solution(a):
    global cnt
    cnt = 0
    def dfs(r,c,s):
        global cnt
        if r == h:
            if sum(col_one) == 0:
                cnt += 1
            return
        if c == w:
            if s % 2 == 0:
                dfs(r + 1, 0, 0)
        else:
            if col_one[c] and b[r][c] == 0:
                b[r][c] = 1
                col_one[c] -= 1
                dfs(r, c + 1, s + 1)
                b[r][c] = 0
                col_one[c] += 1
            dfs(r,c + 1, s)


    h, w = len(a), len(a[0])
    b = [[0] * w for _ in range(h)]
    #a와 b의 열의 1 개수는 같다
    col_one = []
    for i in range(w):
        s = 0
        for j in range(h):
            s += a[j][i]
        col_one.append(s)
    dfs(0,0,0)
    return cnt


solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]])
solution([[1,0,0],[1,0,0]])
solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]])
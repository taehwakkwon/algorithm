import sys
sys.setrecursionlimit(10**7)
def check(s):
    global res
    for i in range(len(s)-1):
        if s[i][0] == s[-1][0] or s[i][1] == s[-1][1] or abs(s[i][0] - s[-1][0]) == abs(s[i][1] - s[-1][1]):
            res.pop()
            return False
    return True


def solve(y,x):
    global res
    if len(res) == N:
        result.add(str(sorted(res)))
        res = []
        return
    for new_y in range(y, N):
        for new_x in range(x, N):
            if (new_y,new_x) not in res:
                res.append((new_y,new_x))
                check(res)
                solve(new_y + 1, new_x + 1)




result = set([])
res = []
move = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
N = 92#int(input())
for i in range(N):
    for j in range(N):
        board = [[0] * N for _ in range(N)]
        if board[i][j] == 0:
            res.append((i,j))
            solve(i,j)
            res = []
print(res)
print(len(set(res)))
print(result, len(result))


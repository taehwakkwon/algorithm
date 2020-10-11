import sys
sys.stdin = open('../now/input.txt')

def dfs(v,s):
    global M
    if v == 10:
        M = max(M, s)
        return
    else:
        for i in range(4):
            if now[i] == -1:
                continue
            elif now[i] in dic:
                before = now[i]
                tmp = now[i]
                for j in range(dice[v]):
                    tmp = dic[tmp]
                if tmp == -1 or tmp not in now:
                    now[i] = tmp
                    dfs(v+1, s + score[tmp])
                    now[i] = before
            else:
                if now[i] + dice[v] >= 21:
                    before = now[i]
                    now[i] = -1
                    dfs(v + 1, s)
                    now[i] = before
                elif now[i] + dice[v] not in now:
                    before = now[i]
                    now[i] += dice[v]
                    dfs(v + 1, s + score[now[i]])
                    now[i] = before

dic = {
    -1:-1,
    5:23,
    23:24,
    24:25,
    25:26,
    10:27,
    27:28,
    28:26,
    15:29,
    29:30,
    30:31,
    31:26,
    26:32,
    32:33,
    33:20,
    20:21,
    21:-1
}

M = 0
score = [i for i in range(0,42,2)] + [0,0] + [13,16,19,25,22,24,28,27,26,30,35,0]
dice = list(map(int, input().split()))
now = [0]*4
dfs(0,0)
print(M)
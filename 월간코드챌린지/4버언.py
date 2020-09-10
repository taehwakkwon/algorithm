from itertools import combinations
def solution(a):
    global cnt
    cnt = 0
    def select(v):
        global cnt
        if v == h:
            cnt += 1
            return
        else:
            for i in ra



    h, w = len(a), len(a[0])
    b = [[0] * w for _ in range(h)]
    #a와 b의 열의 1 개수는 같다
    comb = []
    count = []
    for i in range(w):
        m = 0
        for j in range(h):
            m += a[j][i]
        comb.append(list(combinations(list(range(h)),m)))
        count.append(len(comb[-1]))
    print(comb)
    print(count)

    select(0)

    return cnt

solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]])
solution([[1,0,0],[1,0,0]])
solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]])
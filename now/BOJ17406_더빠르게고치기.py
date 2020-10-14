import sys
sys.stdin = open('input.txt')

from copy import deepcopy
def permutations(v):
    if v >= k:
        permu.append(per[:])
        return
    else:
        for i in range(k):
            if ch[i] == 0:
                ch[i] = 1
                per[v] = i
                permutations(v+1)
                ch[i] = 0

def move(r,c,s,a):
    new_a = [[0]*m for _ in range(n)]
    while s:
        br, bc = r - s, c - s
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            before_value = a[br-1][bc-1]
            for i in range(2*s):
                nr, nc = br + dr, bc + dc
                next_value = a[nr-1][nc-1]
                new_a[nr-1][nc-1] = before_value
                before_value = next_value
                br, bc = nr, nc
        s -= 1
    for i in range(n):
        for j in range(m):
            if new_a[i][j] == 0:
                new_a[i][j] = a[i][j]
    return new_a


def get_min(matrix):
    s = float('inf')
    for i in range(n):
        s = min(s,sum(matrix[i]))
    return s


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rotate = [tuple(map(int, input().split())) for _ in range(k)]
permu = []
ch = [0]*k
per = [-1]*k
permutations(0)
min_val = float('inf')
for per in permu:
    new_a = deepcopy(a)
    for num in per:
        r, c, s = rotate[num]
        new_a = move(r,c,s,new_a)
    min_val = min(min_val, get_min(new_a))
print(min_val)
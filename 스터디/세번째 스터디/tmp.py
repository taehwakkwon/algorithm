import sys
sys.stdin = open('input.txt')

def combinations(v, s, res):
    if v == m:
        result.append(tuple(res))
    else:
        for i in range(s, n):
            res[v] = i
            combinations(v + 1, i + 1, res)

n = 6
m = 2
result = []
res = [0]*m
combinations(0, 0, res)
print(result)
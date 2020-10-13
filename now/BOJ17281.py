import sys
sys.stdin = open('input.txt')
import time
start = time.time()

#선수 9명
# ? ? ? 1 ? ? ~~
import sys
input = sys.stdin.readline

from itertools import permutations
# def permutations(v):
#     if v == 9:
#         permu.append(per[:])
#         return
#     elif v == 3:
#         permutations(v+1)
#     else:
#         for i in range(1,9):
#             if ch[i] == 0:
#                 per[v] = i
#                 ch[i] = 1
#                 permutations(v+1)
#                 ch[i] = 0
#

def solve(batter):
    global M, score
    # def move(n):
    #     s = 0
    #     for i in range(3, -1, -1):
    #         if base[i] == 1 and i + n > 3:
    #             s += 1
    #             base[i] = 0
    #         elif base[i] == 1:
    #             base[i + n] = 1
    #             base[i] = 0
    #     return s
    pivot = 0
    for inning in result:
        out = 0
        a, b, c = 0, 0, 0
        while out < 3:
            if inning[batter[pivot]] == 0:
                out += 1
            elif inning[batter[pivot]] == 1:
                score += c
                a, b, c = 1, a, b
            elif inning[batter[pivot]] == 2:
                score += b + c
                a, b, c = 0, 1, a
            elif inning[batter[pivot]] == 3:
                score += a + b + c
                a = b = 0
                c = 1
            elif inning[batter[pivot]] == 4:
                score += a + b + c + 1
                a = b = c = 0
            pivot = (1+pivot)%9
    M = max(score, M)


M = 0
n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]
# batters = []
# per = [0]*9
# ch = [0]*9
# permu = []
# permutations(0)
for per in permutations(range(1,9),8):
    score = 0
    solve(list(per[:3]) + [0] + list(per[3:]))
print(M)
print(time.time()-start)
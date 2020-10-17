import sys
sys.stdin = open('input.txt')

from collections import deque
def combinations(v,s):
    if v == i:
        group_a.append(res[:])
        res2 = []
        for idx in range(len(people)):
            if idx not in res:
                res2.append(idx)
        group_b.append(res2[:])
    else:
        for idx in range(s, len(people)):
            if res[v] == 0:
                res[v] = idx
                combinations(v+1, idx)
                res[v] = 0

def dfs_a(v,time):
    global min_time_a
    if v >= len_a:
        min_time_a = min(min_time_a,time)
    if time >= min_time_a:
        return
    else:
        if people[v] == stair1:
            on_the_staira[board[stairs[0][0]][stairs[0][1]]].append(people[v])

        else:
            if stair1[0] > people[v][0]:
                people[v][0] -= 1
            elif stair1[0] < people[v][0]:
                people[v][0] += 1
            elif stair1[1] > people[v][1]:
                people[v][1] -= 1
            elif stair1[1] < people[v][1]:
                people[v][1] += 1


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    people = []
    stairs = []
    stair1 = {}
    stair2 = {}
    m = float('inf')
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                people.append((i,j))
                #people[(i,j)] =
            elif board[i][j] >= 2:
                stairs.append((i,j))
    stair1[stairs[0]] = board[stairs[0][0]][stairs[0][1]]
    stair2[stairs[1]] = board[stairs[1][0]][stairs[1][1]]

    group_a = []
    group_b = []
    for i in range(1,10):
        res = [0]*i
        combinations(0,0)

    for coma, comb in zip(group_a,group_b):
        on_the_staira = deque([[] for _ in range(172)])
        on_the_stairb = deque([[] for _ in range(172)])

        len_a = len(coma)
        len_b = len(comb)
        print(coma, comb)
    break


    print(group_a)
    print(group_b)
    print(len(group_b), len(group_a))
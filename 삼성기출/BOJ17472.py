import sys
sys.stdin = open('../now/input.txt')

#다리길이 2 이상
#다리 직선(2개의 섬만 연결!)
#다리 교차 가능(둘다 카운트), 신경 안쓰면 될듯

def coloring(r,c,color):
    for dr, dc in [(0,0),(0,1),(1,0),(0,-1),(-1,0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and colored_map[nr][nc] == 0 and board[nr][nc] == 1:
            colored_map[nr][nc] = color
            coloring(nr,nc,color)

def gen_bridges():
    #가로다리
    for i in range(n):
        start, end = 0, 1
        for j in range(m-1):
            if colored_map[i][start] == 0:
                start += 1
                end += 1
            else:
                if colored_map[i][end] == 0:
                    end += 1
                else:
                    if colored_map[i][start] != colored_map[i][end] and end - start > 2:
                        bridges.append(((i, start), (i, end)))
                    start = end
                    end += 1

    for i in range(m):
        start, end = 0, 1
        for j in range(n-1):
            if colored_map[start][i] == 0:
                start += 1
                end += 1
            else:
                if colored_map[end][i] == 0:
                    end += 1
                else:
                    if colored_map[start][i] != colored_map[end][i] and end - start > 2:
                        bridges.append(((start, i), (end, i)))
                    start = end
                    end += 1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
colored_map = [[0]*m for i in range(n)]
color = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and colored_map[i][j] == 0:
            coloring(i,j,color)
            color += 1

bridges = []
gen_bridges()
def combinations(v,s):
    if v >= color-2:
        result.append(tuple(res))
    else:
        for i in range(s,bridge_cnt):
            if ch[i] == 0:
                ch[i] = 1
                res[v] = i
                combinations(v+1,i+1)
                ch[i] = 0
result = []
bridge_cnt = len(bridges)
res = [0]*(color-2)
ch = [0]*bridge_cnt
combinations(0,0)
# from itertools import combinations
# result = list(combinations(range(bridge_cnt),color-2))
min_value = float('inf')
def check(v):
    if v in island:
        for value in island[v]:
            if visited[value] == 0:
                visited[value] = 1
                check(value)


for com in result:
    island = {i:[] for i in range(1,color)}
    cnt = 0
    for c in com:
        start, end = bridges[c]
        r1, c1 = start
        r2, c2 = end
        cnt += (max(abs(r1-r2), abs(c1-c2)) - 1)
        island[colored_map[r1][c1]].append(colored_map[r2][c2])
        island[colored_map[r2][c2]].append(colored_map[r1][c1])

    visited = [1] + [0]*(color-1)
    check(1)
    if sum(visited) == color:
        min_value = min(min_value, cnt)
if min_value == float('inf'):
    print(-1)
else:
    print(min_value)




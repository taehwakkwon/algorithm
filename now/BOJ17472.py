import sys
sys.stdin = open('input.txt')

#다리길이 2 이상
#다리 직선(2개의 섬만 연결!)
#다리 교차 가능(둘다 카운트), 신경 안쓰면 될듯
def coloring(r,c,color):
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
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
            elif colored_map[i][start] != 0 and colored_map[i][end] != 0 and colored_map[i][end] == colored_map[i][start]:
                start += 1
                end += 1
            elif colored_map[i][start] != 0 and colored_map[i][start] == colored_map[i][end]:
                end += 1
            else:
                if colored_map[i][start] != 0 and  colored_map[i][start] != colored_map[i][end] and colored_map[i][end] != 0:
                    if end - start > 1:
                        horizontal[(i,start)] = (i,end)
                    start = end
                    end += 1
                else:
                    end += 1
    for i in range(m):
        start, end = 0, 1
        for j in range(n-1):
            if colored_map[start][i] == 0:
                start += 1
                end += 1
            elif colored_map[start][i] != 0 and colored_map[end][i] != 0 and colored_map[end][i] == colored_map[start][i]:
                start += 1
                end += 1
            elif colored_map[start][i] != 0 and colored_map[start][i] == colored_map[end][i]:
                end += 1
            else:
                if colored_map[start][i] != 0 and colored_map[start][i] != colored_map[end][i] and colored_map[end][i] != 0:
                    if end - start > 1:
                        vertical[(start,i)] = (end, i)
                    start = end
                    end += 1
                else:
                    end += 1



horizontal = {}
vertical = {}

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
for key, value in horizontal.items():
    bridges.append((key,value))

for key, value in vertical.items():
    bridges.append((key,value))

def dfs(v):
    global min_value
    if v == color - 1:
        min_value = min(min_value, )


min_value = 0
island = [1] + [0]*(color-1)
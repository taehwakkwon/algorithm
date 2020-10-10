import sys
sys.stdin=open('input.txt')

from collections import defaultdict
def aged():
    next_trees = defaultdict(list)
    for x, y in list(trees.keys()):
        for i in range(len(trees[(x,y)])):
            if board[x][y] >= trees[(x,y)][i]:
                board[x][y] -= trees[(x,y)][i]
                next_trees[(x,y)].append(trees[(x,y)][i] + 1)
                if (trees[(x,y)][i]+1) % 5 == 0:
                    for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                        if 0 <= x + dx < n and 0 <= y + dy < n:
                            next_trees[(x+dx, y+dy)] = [1] + trees.get((x+dx, y+dy), [])

            else:
                board[x][y] += (trees[(x, y)][i] // 2)

    for i in range(n):
        for j in range(n):
            board[i][j] += a[i][j]
    return next_trees


n,m,k = map(int, input().split())
board = [[5]*n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]

trees = defaultdict(list)

for i in range(m):
    x,y,z = map(int, input().split())
    trees[(x-1,y-1)].append(z)

for i in range(k):
    trees = aged()

cnt = 0
for key in trees:
    cnt += len(trees[key])
print(trees)


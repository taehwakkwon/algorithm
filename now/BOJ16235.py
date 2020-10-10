import sys
sys.stdin = open('input.txt')
import time

start = time.time()
import sys
input = sys.stdin.readline
from collections import deque, defaultdict
def aged(iter):
    die = []
    breed = []

    for x, y in trees:
        for i in range(len(trees[(x,y)])):
            if board[x][y] >= trees[(x,y)][i]:
                board[x][y] -= trees[(x,y)][i]
                trees[(x,y)][i] += 1
                if trees[(x,y)][i] % 5 == 0:
                    breed.append((x,y,i))
            else:
                die.append((x,y,i))
    return die, breed

def dead(die_list):
    for x,y,i in die_list[::-1]:
        board[x][y] += (trees[(x, y)][i] // 2)
        if len(trees[(x, y)]) > 1:

            del trees[(x, y)][i]
            #trees[(x, y)] = sorted(trees[(x, y)])
        else:
            del trees[(x, y)]


def breeding(breed):
    for x,y,i in breed:
        for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                trees[(x + dx,y + dy)].appendleft(1)

def fertilize():
    for i in range(n):
        for j in range(n):
            board[i][j] += a[i][j]

n,m,k = map(int, input().split())
board = [[5]*n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
trees = defaultdict(list)

for i in range(m):
    x,y,z = map(int, input().split())
    trees[z].append((x,y))

now = 0
while k:
    iter = 0
    for key in trees:
        iter = max(key%5)
    if (5-iter) > k:
        die, breed = aged(k)
    else:
        die, breed = aged(5-iter)








trees.keys()
print(trees)

# for i in range(k):
#     die, breed = aged()
#     if die:
#         dead(die)
#     if breed:
#         breeding(breed)
#     fertilize()
cnt = 0
for key in trees:
    cnt += len(trees[key])
print(cnt)


print(time.time()-start)
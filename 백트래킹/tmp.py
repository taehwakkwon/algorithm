import sys
sys.stdin = open('input.txt')
import time
start = time.time()
import sys
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
input = stdin.readline
N = int(input())
Chess = [list(map(int, input().split())) for _ in range(N)]
Count = [0] * 2
Criterion = 0
Left = [0] * 21
Right = [0] * 21
def isPromising(r, c):
    if Chess[r][c] and Left[r + c] == 0 and Right[r - c + N] == 0:

        return True

    else:

        return False


def dfs(r, c, count):
    Count[Criterion] = max([Count[Criterion], count])
    print(bishop)

    if c >= N:
        r += 1

        c = Criterion ^ (r % 2)

    if r >= N:
        return

    if isPromising(r, c):
        Left[r + c] = Right[r - c + N] = 1
        bishop.append((r,c))

        dfs(r, c + 2, count + 1)

        bishop.remove((r,c))
        Left[r + c] = Right[r - c + N] = 0

    dfs(r, c + 2, count)


bishop = []
dfs(0, 0, 0)

Criterion = 1

dfs(0, 1, 0)
print()
print(Count[0] + Count[1])

print(time.time() - start)
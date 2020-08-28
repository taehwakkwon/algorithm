import sys
sys.stdin = open('sample_input.txt')
import sys
sys.setrecursionlimit(10**7)
def dfs(y, x):
    print(y,x)
    if y == 0:
        print('#%d %d' %(t, x))
        return
    else:
        ladder[y][x] = 0

        for dy, dx in move:
            if 0 <= y+dy < 100 and 0 <= x + dx < 100 and  ladder[y + dy][x + dx] == 1:
                dfs(y + dy, x + dx)
                return


move = [(0, -1), (0, 1), (-1, 0)]
T = 10
for t in range(1, T + 1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[99][i] == 2:
            dfs(99,i)
            break
    break
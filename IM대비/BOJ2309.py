import sys
sys.stdin = open('input.txt')

import sys
def dfs(v,s):
    if s < 100:
        return
    if v == 7:
        if s == 100:
            for i in range(9):
                if check[i] == 1:
                    print(heights[i])
            sys.exit()

    else:
        for i in range(9):
            if check[i] == 1:
                check[i] = 0
                dfs(v - 1, s - heights[i])
                check[i] = 1


heights = []
for i in range(9):
    heights.append(int(input()))
heights.sort()
check = [1]*9
dfs(9,sum(heights))
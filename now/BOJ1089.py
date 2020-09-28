import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
numbers = [[7,5,5,5,7],[1,1,1,1,1],[7,1,7,4,7],[7,1,7,1,7],[5,5,7,1,1],[7,4,7,1,7],[7,4,7,5,7],[7,1,1,1,1],[7,5,7,5,7],[7,5,7,1,7]]
N = int(input())
ans = [[] for _ in range(N)]
lights = [input() for i in range(5)]
num = [[0] for _n in range(N)]
for i in range(5):
    for j in range(N):
        tmp = 0
        for k in range(3):
            if k+j*3+j < len(lights[i]) and lights[i][k+j*3+j] == '#':
                tmp += 1<<(2-k)
        num[j].append(tmp)

for i in range(N): #N
    for k in range(10):
        for j in range(1,6):
            if numbers[k][j-1] != (num[i][j] | numbers[k][j-1]):
                break
        else:
            ans[i].append(k)
s = 0
for i in range(N):
    if ans[i]:
        s += 10**(N-i-1)*sum(ans[i])/len(ans[i])
    else:
        print(-1)
        sys.exit()
print(s)

import sys
sys.stdin = open('../발표/창고다각형.txt')

import sys
n = int(sys.stdin.readline())
pillar = []
for i in range(n):
    l, h = map(int, sys.stdin.readline().split())
    pillar.append((l, h))
pillar.sort()

roof = [0]*(pillar[-1][0]+1)
for l, h in pillar:
    roof[l] = h
max_idx = roof.index(max(roof))
height = 0
for left in range(max_idx):
    if height < roof[left]:
        height = roof[left]
    else:
        roof[left] = height

height = 0
for right in range(len(roof)-1,max_idx,-1):
    if height < roof[right]:
        height = roof[right]
    else:
        roof[right] = height

print(sum(roof))




import sys
sys.stdin = open('input.txt','r')

import sys
N, M = map(int, sys.stdin.readline().split())

pocketmon = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    pocketmon[i+1] = name

pocketmon_name = {}
for key, value in sorted(pocketmon.items(), key = lambda x : x[1]):
    pocketmon_name[value] = key

for i in range(M):
    m = sys.stdin.readline().strip()
    if m.isdigit():
        print(pocketmon[int(m)])
    else:
        print(pocketmon_name[m])
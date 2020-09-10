import sys
sys.stdin=open('input.txt')
import time
start = time.time()
from collections import deque

def dfs(pre, v):
    if not queue:
        queue.append([a,b])
    



cnt = 0
n = int(input())
M = 0
queue = deque([])
for i in range(n):
    pivot = len(queue) // 2
    a, b = map(int, input().split())



infos = [list(map(int, input().split())) for _ in range(n)]
room = []
print(infos)
print(room)
print(len(room))
print(time.time()-start)
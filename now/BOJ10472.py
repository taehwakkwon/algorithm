import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(board):
    queue = deque([board])
    while queue:
        board = queue.popleft()
        for i in range(9):


                pass




T = int(input())
for t in range(T):
    targit = ''
    for i in range(3):
        targit += input().replace('*','1').replace('.','0')
    targit = list(map(bool, map(int,list(targit))))
    board = [False]*9
    #bfs(board)
    print(board)

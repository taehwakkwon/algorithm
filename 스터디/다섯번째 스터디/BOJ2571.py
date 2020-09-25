import sys
sys.stdin = open('input.txt')

MAX = 101
n = int(input())
board = [[0]*MAX for _ in range(MAX)]
points = []
dr = [1,0,-1,0]
dc = [0,1,0,-1]
for i in range(n):
    a, b = map(int, input().split())
    points.extend([(a,b),(a+10,b),(a,b+10),(a+10,b+10)])
    for p in range(a, a + 10):
        for q in range(b, b + 10):
            board[p][q] = 1
for r in board:
    print(*r)
print(points)

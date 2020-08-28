import sys
sys.stdin = open('input.txt')

board = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        for p in range(3):
            for q in range(3):
                print(i//3*3+p, j//3*3+q,'/', end = ' ')
            print()
        print()
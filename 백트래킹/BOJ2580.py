import sys
sys.stdin = open('input.txt')
import sys
sys.setrecursionlimit(10**7)



def check(y, x):


def dfs(y, x):
    for i in range(9):
        for j in range(9):
            if row_board[i][j] == 0:
                c = [0]*10
                for p in range(3):
                    for q in range(3):
                        c[row_board[i//3*3 + p][j//3*3 + q]] = 1
                for k in range(1, 10):
                    if row_board[i].count(k) == 0 and col_board[j].count(k) == 0 and c[k] == 0:
                        row_board[i][j] = k
                        col_board[j][i] = k
                        dfs(0, 0)
                        row_board[i][j] = 0
                        col_board[j][i] = 0
    if check():
        for r in row_board:
            print(*r)
        sys.exit()

row_board = [list(map(int, input().split())) for _ in range(9)]
col_board = transpose(row_board)



dfs(0,0)
'''
4 6 7 8 0 0 2 0 9
3 4 9 8 2 0 5 0 0
2 1 4 9 5 3 6 8 0
3 7 1 2 9 4 0 0 6
1 3 6 0 0 0 0 0 8
2 6 7 8 4 0 0 5 1
1 3 7 5 8 4 0 9 0
1 2 3 0 7 9 0 4 0
5 4 9 0 0 2 7 6 0

4 6 7 8 0 0 2 0 9
3 4 9 8 2 0 5 0 0
2 1 4 9 5 3 6 8 0
3 7 1 2 9 4 0 0 6
1 3 6 0 0 0 0 0 8
2 6 7 8 4 0 0 5 1
1 3 7 5 8 4 0 9 0
1 2 3 0 7 9 0 4 0
5 4 9 3 0 2 7 6 0
'''
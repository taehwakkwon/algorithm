import sys
sys.stdin = open('input.txt')


import sys
def check():
    bingo = 0
    for i in range(5):
        if all(check_col[i]):
            bingo += 1
        if all(check_row[i]):
            bingo += 1

    for i in range(5):
        if check_row[i][i] == True:
            continue
        break
    else:
        bingo += 1

    for i in range(5):
        if check_row[i][4-i] == True:
            continue
        break
    else:
        bingo += 1
    return bingo

board = [list(map(int, input().split())) for _ in range(5)]
check_row = [[False]*5 for _ in range(5)]
check_col = [[False]*5 for _ in range(5)]


cnt = 0

for i in range(5):
    for number in list(map(int, input().split())):
        cnt += 1
        for j in range(5):
            if number in board[j]:
                c = board[j].index(number)
                check_row[j][c] = check_col[c][j] = True
        if check() >= 3:
            print(cnt)
            sys.exit()





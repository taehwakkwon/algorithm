import sys
sys.stdin = open('input.txt')
def check(i, j):
    num_count = [0] * 9
    for dy, dx in [(0, 1), (1, 0), (0, -1), (0, -1)]:
        new_y, new_x = i, j
        while 0 <= new_y < 9 and 0 <= new_x < 9:
            if board[new_y][new_x] != 0:
                num_count[board[new_y][new_x] - 1] += 1
            new_y += dy
            new_x += dx
    if num_count.count(0) == 1:
        return num_count
    new_y, new_x = i//3, j//3
    for p in range(3):
        for q in range(3):
            if board[new_y*3+p][new_x*3+q] != 0:
                num_count[board[new_y*3+p][new_x*3+q] - 1] += 1
    return num_count




def solve(y, x):
    if (y, x) == (8, 9):
        return
    if x == 9:
        solve(y+1,0)
    else:
        if board[y][x] == 0:
            count = check(y,x)
            for i in range(9):
                if count[i] == 0:
                    board[y][x] = i + 1
        solve(y, x + 1)



board = [list(map(int, input().split())) for _ in range(9)]
solve(0,0)
for r in board:
    print(*r)
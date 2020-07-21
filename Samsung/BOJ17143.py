#import sys
#sys.stdin = open('input.txt','r')

import sys
def shark_move():
    global board
    new_board = [[0]*(C) for _ in range(R)]
    for j in range(len(infos)):
        board[infos[j][0]][infos[j][1]] = 0
        if infos[j][-1] == 0:
            continue
        if board[infos[j][0]][infos[j][1]] != infos[j][-1]:
            infos[j][-1] = 0
            continue
        speed = infos[j][2]
        direction = infos[j][3]
        size = infos[j][-1]
        if direction <= 2:
            speed = speed%((R-1)*2)
        else:
            speed = speed%((C-1)*2)
        while speed:
            if infos[j][0] + dy[direction] == -1 and direction == 1:
                direction = dir(direction)
            elif infos[j][0] + dy[direction] == R and direction == 2:
                direction = dir(direction)
            elif infos[j][1] + dx[direction] == C and direction == 3:
                direction = dir(direction)
            elif infos[j][1] + dx[direction] == -1 and direction == 4:
                direction = dir(direction)
            infos[j][3] = direction
            infos[j][0] += dy[direction]
            infos[j][1] += dx[direction]
            speed -= 1
    print(board)
    print(infos)
    for j in range(len(infos)):
        if infos[j][-1] == 0:
            continue
        if board[infos[j][0]][infos[j][1]] < infos[j][-1]:
            print(infos[j][-1])
            board[infos[j][0]][infos[j][1]] = infos[j][-1]

def dir(d):
    if d == 1:return 2
    elif d == 2:return 1
    elif d == 3:return 4
    elif d == 4:return 3

def get_shark():
    for j in range(R):
        if board[j][i] != 0:
            res = board[j][i]
            board[j][i] = 0
            return res
    else:
        return 0


if __name__ == "__main__":
    dx = [0,0,0,1,-1]
    dy = [0,-1,1,0,0]

    R,C,M = map(int, sys.stdin.readline().split())

    board = [[0]*(C) for _ in range(R)]
    infos = []
    for i in range(M):
        #r,c,s,d,z
        r,c,s,d,z = map(int, sys.stdin.readline().split())
        r -= 1
        c -= 1
        infos.append([r, c, s, d, z])
        if board[r][c] < z:
            board[r][c] = z
            continue
    weight = 0
    for i in range(C):
        number = get_shark()
        weight += number
        print(number)
        shark_move()
    print(weight)
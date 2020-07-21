import sys
sys.stdin = open('input.txt','r')

def check_room():
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0:
                if room[i][j] == -1:
                    if (i,j) not in air_filter:
                        air_filter.append((i,j))
                    new_room[i][j] = -1
                    continue
                diffuse(i,j)
    return new_room

def diffuse(i,j):
    add = room[i][j] // 5
    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if x + i < 0 or x + i >= R or y + j < 0 or y + j >= C or room[x + i][y + j] == -1:
            continue
        new_room[x+i][y+j] += add
        room[i][j] -= add
    new_room[i][j] += room[i][j]
    room[i][j] = 0

def clean_up():
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    room[air_filter[0][0]-1][0] = 0
    now = (air_filter[0][0]-1,0)
    direction = 0
    while now != (air_filter[0][0],air_filter[0][1]+1):
        while True:
            if (now[0],now[1]) == (air_filter[0][0],1):
                break
            if now == (0,0)  or now == (0,C-1) or now == (air_filter[0][0],C-1):
                direction += 1
            new_loc = (dy[direction]+now[0],dx[direction]+now[1])
            room[now[0]][now[1]], room[new_loc[0]][new_loc[1]] = room[new_loc[0]][new_loc[1]], room[now[0]][now[1]]
            now = new_loc

def clean_down():
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    room[air_filter[1][0]+1][0] = 0
    now = (air_filter[1][0]+1,0)
    direction = 0
    while now != (air_filter[1][0],air_filter[1][1]+1):
        while True:
            if (now[0],now[1]) == (air_filter[1][0],1):
                break
            if now == (R-1,0)  or now == (R-1,C-1) or now == (air_filter[1][0],C-1):
                direction += 1
            new_loc = (dy[direction]+now[0],dx[direction]+now[1])
            room[now[0]][now[1]], room[new_loc[0]][new_loc[1]] = room[new_loc[0]][new_loc[1]], room[now[0]][now[1]]
            now = new_loc

if __name__ == "__main__":
    air_filter = []
    dy = [0,-1,0,1]
    dx = [1,0,-1,0]
    R,C,T = map(int, sys.stdin.readline().split())
    room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    for i in range(T):
        new_room = [[0] * C for _ in range(R)]
        room = check_room()
        clean_up()
        clean_down()
    count = 0
    for j in room:
        count += sum(j)
    print(count+2)
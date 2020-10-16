import sys
sys.stdin = open('../now/input.txt')
#엇갈리는 경우!
#3개 충돌할 때 => 충돌하는곳 위치를 정하기
move = [(0,1), (0,-1),(-1,0),(1,0)]
def go():
    global energy
    dic = {}
    for i in range(len(infos)-1,-1,-1):
        x,y,direc,k = infos[i]
        nx, ny = x + move[direc][0], y + move[direc][1]
        if -2000 < nx < 2000 and -2000 < ny < 2000:
            infos[i][0],infos[i][1] = nx, ny
            dic[(nx,ny)] = dic.get((nx,ny),0) + 1
        else:
            infos.pop(i)

    for i in range(len(infos)-1,-1,-1):
        x,y,direc,k = infos[i]
        if dic[(x,y)] > 1:
            energy += k
            infos.pop(i)


T = int(input())
for t in range(1, 1+T):
    n = int(input())
    energy = 0
    infos = []
    loc_infos = {}
    for i in range(n):
        x,y,direc, k = map(int ,input().split())
        x *= 2
        y *= 2
        infos.append([x,y,direc,k])
        loc_infos[(x,y)] = 1


    for a in range(4004):
        go()
    print('#%d %d' %(t, energy))
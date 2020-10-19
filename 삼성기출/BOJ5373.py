import sys
sys.stdin = open('../now/input.txt')

#윗면, 아랫면, 앞면, 뒷면, 왼쪽, 오른쪽
#흰,    노,    빨,   오,  초,   파
U = {1:3,2:4,3:5,4:6,5:7,6:8,7:1,8:2,
     27:43,26:42,25:41,43:19,42:18,41:17,19:35,18:34,17:33,35:27,34:26,33:25}
D = {9:11,10:12,11:13,12:14,13:15,14:16,15:9,16:10,
    23:47,22:46,21:45,47:31,46:30,45:29,31:39,30:38,29:37,39:23,38:22,37:21}
F = {17:19,18:20,19:21,20:22,21:23,22:24,23:17,24:18,
     7:41,6:48,5:47,41:11,48:10,47:9,11:37,10:36,9:35,37:7,36:6,35:5}
B = {25:27,26:28,27:29,28:30,29:31,30:32,31:25,32:26,
     3:33,2:40,1:39,33:15,40:14,39:13,15:45,14:44,13:43,45:3,44:2,43:1}
L = {33:35,34:36,35:37,36:38,37:39,38:40,39:33,40:34,
     1:17,8:24,7:23,17:9,24:16,23:15,9:29,16:28,15:27,29:1,28:8,27:7}
R = {41:43,42:44,43:45,44:46,45:47,46:48,47:41,48:42,
     5:25,4:32,3:31,25:13,32:12,31:11,13:21,12:20,11:19,21:5,20:4,19:3}

color = ['w','y','r','o','g','b']
T = int(input())
for t in range(1, T + 1):
    n = int(input())
    cube = ['w']
    for col in color:
        cube.extend([col] * 8)

    next_cube = ['w'] + [''] * 48
    how = list(input().split())
    for item in how:
        loc, direc = item
        if loc == 'U':
            if direc == '+':
                for key, value in U.items():
                    next_cube[value] = cube[key]
            else:
                for key, value in U.items():
                    next_cube[key] = cube[value]
        elif loc == 'D':
            if direc == '+':
                for key, value in D.items():
                    next_cube[value] = cube[key]
            else:
                for key, value in D.items():
                    next_cube[key] = cube[value]
        elif loc == 'F':
            if direc == '+':
                for key, value in F.items():
                    next_cube[value] = cube[key]
            else:
                for key, value in F.items():
                    next_cube[key] = cube[value]
        elif loc == 'B':
            if direc == '+':
                for key, value in B.items():
                    next_cube[value] = cube[key]
            else:
                for key, value in B.items():
                    next_cube[key] = cube[value]
        elif loc == 'L':
            if direc == '+':
                for key, value in L.items():
                    next_cube[value] = cube[key]
            else:
                for key, value in L.items():
                    next_cube[key] = cube[value]

        elif loc == 'R':
            if direc == '+':
                for key, value in R.items():
                    next_cube[value] = cube[key]
            else:
                for key, value in R.items():
                    next_cube[key] = cube[value]
        for i in range(len(next_cube)):
            if next_cube[i] == '':
                next_cube[i] = cube[i]
        cube = next_cube[:]
    print(''.join(cube[1:4]))
    print('%sw%s' %(cube[8],cube[4]))
    print(''.join(cube[5:8][::-1]))
import sys
sys.stdin = open('input.txt')
def gen_points(square):
    points = []
    for i in range(0,4,2):
        points.append((square[i],square[i+1]))
        points.append((square[i],square[3-i]))
    return points



for i in range(4):
    squares = list(map(int, input().split()))
    square_a = squares[:4]
    square_b = squares[4:]

    rows_a = []
    for i in range(square_a[0],square_a[2] + 1):
        rows_a.append((square_a[1],i))
        rows_a.append((square_a[3], i))
    rows_b = []
    for i in range(square_b[0], square_b[2] + 1):
        rows_b.append((square_b[1], i))
        rows_b.append((square_b[3], i))

    cols_a = []
    for i in range(square_a[1], square_a[3] + 1):
        cols_a.append((i, square_a[0]))
        cols_a.append((i, square_a[2]))

    cols_b = []
    for i in range(square_b[1], square_b[3] + 1):
        cols_b.append((i, square_b[0]))
        cols_b.append((i, square_b[2]))

    points_a = gen_points(square_a)
    points_b = gen_points(square_b)

    res = 'd'
    if points_a == points_b:
        print('a')
    else:
        for i in range(4):
            if points_b[0][0] < points_a[i][0] < points_b[2][0] and points_b[0][1] < points_a[i][1] < points_a[2][1]:
                res = 'a'
                break
            if points_a[0][0] < points_b[i][0] < points_a[2][0] and points_a[0][1] < points_b[i][1] < points_b[2][1]:
                res = 'a'
                break
        if res == 'd':
            for i in range(4):
                flag = 0
                for j in range(4):
                    if points_a[i] == points_b[j]:
                        flag += 1

                if flag == 1:
                    res = 'c'
                    break
                elif flag == 2:
                    #a인지 b인지
                    res = 'b'
                    break
        if res == 'd':
            if len(set(rows_a)&set(rows_b)) >= 2 or len(set(cols_a) & set(cols_b)):
                res = 'b'

        print(res)




'''
a
a in b or b in a
모서리 중 1개가 다른 사각형 내부에 있을 때
b
한 모서리의 x 혹은 y좌표가 겹치고 모서리가 겹치지 않을 때
c
모서리가 겹칠 때
d
else


'''
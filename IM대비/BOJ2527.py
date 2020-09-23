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
    points_a = gen_points(square_a)
    points_b = gen_points(square_b)

    if (len(set(points_a)&set(points_b)) == 1):
        print('c')
    elif square_a[2] < square_b[0] and square_a[3] < square_b[1]:
        print('a')
    elif (square_a[0] > square_b[2] or square_a[1] > square_b[3] or square_a[2] < square_b[0] or square_a[3] < square_b[
        1]):
        print('d')
    elif (square_b[0] > square_a[2] or square_b[1] > square_a[3] or square_b[2] < square_a[0] or square_b[3] < square_a[
        1]):
        print('d')

    else:
        print('b')
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
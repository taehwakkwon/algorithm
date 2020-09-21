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
    print(set(points_a) & set(points_b))
    res = ''
    if len(set(points_a) & set(points_b)) == 1:
        res = 'c'






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
import sys
sys.stdin = open('input.txt')
def gen_square(x,y,z,w):
    square = []
    for i in range(x, z+1):
        for j in range(y, w + 1):
            square.append((i,j))
    return square

def gen_points(square):
    points = []
    for i in range(0,4,2):
        points.append((square[i],square[i+1]))
        points.append((square[i],square[3-i]))
    return points



for i in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    square_a = set(gen_square(a,b,c,d))
    square_b = set(gen_square(e,f,g,h))
    
    points_a = gen_points(square_a)
    points_b = gen_points(square_b)

    res = ''

    intersect = square_a & square_b
    if square_a == square_b and :
        res = 'a'
    elif len(intersect) == 1:
        res = 'c'
    elif len(intersect) == 0:
        res = 'd'

    if

#2 -> b or a
#3

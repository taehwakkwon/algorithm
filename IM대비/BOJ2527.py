import sys
sys.stdin = open('input.txt')

for i in range(4):
    squares = list(map(int, input().split()))
    square_a = squares[:4]
    square_b = squares[4:]
    left = max(square_a[0],square_b[0])
    right = min(square_a[2],square_b[2])
    top = min(square_a[3], square_b[3])
    bottom = max(square_a[1], square_b[1])

    width = right - left
    height = top - bottom
    
    if width == 0 and height == 0:
        print('c')
    elif width == 0 or height == 0:
        print('b')
    elif width < 0 or height < 0:
        print('d')
    else:
        print('a')


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
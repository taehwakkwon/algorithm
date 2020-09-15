import sys
sys.stdin = open('input.txt')

shuffle = list(map(int, input().replace('A','1').replace('B','2').replace('C','3')))
ball = [1,0,0]
for i in range(len(shuffle)):
    if shuffle[i] == 1:
        ball[0], ball[1] = ball[1], ball[0]
    elif shuffle[i] == 2:
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[0], ball[2] = ball[2], ball[0]
print(ball.index(1) + 1)

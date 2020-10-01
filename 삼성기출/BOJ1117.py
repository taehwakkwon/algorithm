import sys
sys.stdin = open('../now/input.txt')

#W, H 10^9
W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
if W >= 2*f:
    if x1 <= f <= x2:
        print(W*H - (x2 - x1 + f - x1) * (y2 - y1) * (c + 1))
    elif f <= x1:
        print(W*H - (x2 - x1) * (y2 - y1) * (c + 1))
    elif f >= x2:
        print(W*H - (x2 - x1) * (y2 - y1) * (c + 1) * 2)
else:
    if x1 <= W - f <= x2:
        print(W*H - (((W - f) - x1) * (y2 - y1) + (x2 - x1) * (y2 - y1)) * (c + 1))
    elif x1 >= W - f:
        print(W*H - (x2 - x1) * (y2 - y1) * (c + 1))
    elif x2 <= W - f:
        print(W*H - (x2 - x1) * (y2 - y1) * (c + 1) * 2)

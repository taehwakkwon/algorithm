def spin(bf, direction):
    global right, left
    direction_right = direction
    direction_left = direction
    while left >= 0:
        if mag[left + 1][-2] != mag[left][2]:
            direction_left = -direction_left
            ch[left] = direction_left
            left -= 1
        elif mag[left + 1][-2] == mag[left][2]:
            break
    while right < 4:
        if mag[right - 1][2] != mag[right][-2]:
            direction_right = -direction_right
            ch[right] = direction_right
            right += 1
        elif mag[right - 1][2] == mag[right][-2]:
            break
    for i in range(4):
        if ch[i] == 1:
            mag[i].rotate(1)
        elif ch[i] == -1:
            mag[i].rotate(-1)
    return


from collections import deque

T = int(input())
res = [0] * T
for i in range(T):
    K = int(input())
    mag = [0] * 4
    cnt = 0
    for j in range(4):
        mag[j] = deque(list(map(int, input().split())))
    for j in range(K):
        ch = [0] * 4
        m, d = map(int, input().split())
        m -= 1
        right = m + 1
        left = m - 1
        ch[m] = d
        spin(m, d)
    for p in range(4):
        cnt += mag[p][0] * (2 ** p)
    res[i] = cnt
for i in range(T):
    print('#%d %d' % (i + 1, res[i]))
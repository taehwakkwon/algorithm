import sys
sys.stdin = open('sample_input.txt')

T = 10
for t in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while dump:
        dump -= 1
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        if all([bool(boxes[0] == x) for x in boxes[1:]]):
            print('#%d %d' % (t, 0))
            break
    else:
        print('#%d %d' %(t, max(boxes) - min(boxes)))
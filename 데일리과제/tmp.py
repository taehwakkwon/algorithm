
import sys
sys.stdin = open('sample_input.txt','r')
t = 10
for i in range(t):
    n = int(input())
    #print(n)
    boxes = list(map(int, input().split()))
    #print(boxes)
    sum_house = 0
    for i in range(2, len(boxes) - 2):
        if boxes[i] > max(boxes[i + 1], boxes[i + 2]) and boxes[i] > max(boxes[i - 1], boxes[i - 2]):
            house = max(max(boxes[i + 1], boxes[i + 2]), max(boxes[i - 1], boxes[i - 2]))
        if house < boxes[i]:
            sum_house = house - boxes[i]
    print('#{} {}'.format(i-1, sum_house))
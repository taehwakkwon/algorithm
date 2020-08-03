import sys
sys.stdin = open('input.txt','r')

if __name__ == "__main__":
    t = int(input())
    dp = [0]*12
    dp[2] = 1
    dp[3] = 3
    for i in range(t):
        n = int(input())
        cnt = 0
        for j in range(4,n):
            dp[j] = dp[j - 1] * 2 + 1
    print(dp)


1: 0
2: 1
3: 3
4: 7
5:
11111: 1
2111: 4
311: 3
import sys
sys.stdin = open('input1.txt','r')
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
        else:
        sum_house = house - boxes[i]
    print('#{} {}'.format(i-1, sum_house))
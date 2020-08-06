import sys
sys.stdin = open('input.txt')
for tc in range(1,11):
    N = int(input())
    arr = []
    for i in range(1, 101):
        arr.append(list(map(int, input().split())))
print(arr)
        #

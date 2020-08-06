from sys import stdin
stdin = open('input.txt')
n = int(input())
numbers = list(map(int,input().split()))
dp = [0]*n
mid = n//2

for tc in range(1,11):
    N = int(input())
    arr = []
    for i in range(1, 101):
        arr.append(list(map(tin, input().split())))
        print(arr)
        #
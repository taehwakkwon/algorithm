import sys
sys.stdin = open('input.txt','r')

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dic_num = {}
for num in numbers:
    dic_num[num] = dic_num.get(num, 0) + 1
m = int(input())
cards = list(map(int,input().split()))
for num in cards:
    print(dic_num.get(num,0), end = ' ')



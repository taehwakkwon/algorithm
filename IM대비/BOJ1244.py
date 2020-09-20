import sys
sys.stdin = open('input.txt')

def swch(idx):
    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0


n = int(input()) #100이하
switch = [0] + list(map(int, input().split())) #switch status
students_number = int(input())
for i in range(students_number):
    sex, num = map(int, input().split()) #s:1 남, 2 여
    if sex == 1:
        for j in range(num, n + 1, num):
            swch(j)
    else:
        swch(num)
        left = num - 1
        right = num + 1
        while right <= n and left > 0 and switch[right] == switch[left]:
            swch(left)
            swch(right)
            left -= 1
            right += 1

switch.pop(0)
for i in range(0,n,20):
    print(*switch[i:i+20])



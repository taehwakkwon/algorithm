import sys
sys.stdin = open('input.txt')
import math
n, k = map(int, input().split())
male_students = [0]*7
female_students = [0]*7
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        female_students[b] += 1
    else:
        male_students[b] += 1

cnt = 0
for i in range(1,7):
    cnt += math.ceil(female_students[i]/k)
    cnt += math.ceil(male_students[i] / k)
print(cnt)
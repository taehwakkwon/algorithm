import sys
sys.stdin = open('input.txt')


n = int(input())
numbers = list(map(int, input().split()))
students = list(range(1, n + 1))
for i in range(len(numbers)):
    students.insert(i - numbers[i], students.pop(i))

print(*students)
import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
start = 0
end = k
s = sum(numbers[start:end])
M = s
for i in range(n-k):
    s -= numbers[start]
    s += numbers[end]
    start += 1
    end += 1
    if s > M:
        M = s
print(M)


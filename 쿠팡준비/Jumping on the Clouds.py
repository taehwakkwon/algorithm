n = int(input())
c = list(map(int, input().split()))
idx = jump = 0
while idx < len(c)-1:
    if idx + 2 < len(c) and c[idx + 2] == 1:
        idx += 1
    else:
        idx += 2
    jump += 1

print(jump)



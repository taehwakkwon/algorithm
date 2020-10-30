import sys
sys.stdin = open('input.txt')

operaters = [ '+', '-', '*', '/' ]
def dfs(v,s):
    global M, m
    if v == n:
        M = max(M, s)
        m = min(m, s)
        return
    else:
        if operater_nums[0] > 0:
            operater_nums[0] -= 1
            dfs(v+1, s + numbers[v])
            operater_nums[0] += 1
        if operater_nums[1] > 0:
            operater_nums[1] -= 1
            dfs(v + 1, s - numbers[v])
            operater_nums[1] += 1
        if operater_nums[2] > 0:
            operater_nums[2] -= 1
            dfs(v + 1, s * numbers[v])
            operater_nums[2] += 1
        if operater_nums[3] > 0:
            operater_nums[3] -= 1
            dfs(v + 1, int(s / numbers[v]))
            operater_nums[3] += 1


T = int(input())
for t in range(1, T+1):
    n = int(input())
    operater_nums = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    M, m = -float('inf'), float('inf')
    dfs(1,numbers[0])
    print('#%d %d' %(t, M-m))

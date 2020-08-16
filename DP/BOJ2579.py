import sys
sys.stdin = open('input.txt')

# 한 번에 한계단, 또는 두 계단
# 연속된 세개x
# 마지막 계단
#

n = int(input())
steps = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(steps))
    sys.exit()
elif n == 3:
    print(max(steps[0] + steps[2], steps[1] + steps[2]))
else:
    dp = [0]*(302)
    dp[:3] = [steps[0], steps[0]+steps[1], max(steps[0]+steps[2], steps[1]+steps[2])]
    for i in range(3,n):
        dp[i] = max(steps[i] + steps[i-1] + dp[i-3], steps[i] + dp[i-2])
    print(dp[n-1])




# def dfs(v,s,b):
#     global M
#     if v >= n:
#         if b >= 3:
#             return
#         else:
#             if M < s:
#                 M = s
#             return
#     else:
#         if v == n-1:
#             dfs(v+1,s+steps[v], b + 1)
#         else:
#             if b < 2:
#                 dfs(v+1,s+steps[v], b+1)
#             dfs(v+2,s+steps[v],1)
#
#
#
# n = int(input())
# steps = [int(input()) for _ in range(n)]
# M = 0
# dfs(0,0,1)
# dfs(1,0,1)
# print(M)

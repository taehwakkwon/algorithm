import sys
sys.stdin = open('input.txt')

from copy import deepcopy
import sys
sys.setrecursionlimit(10**8)
def reverse(num_string, f):
    return num_string[:f] + num_string[f:f+k][::-1] + num_string[f+k:]

def dfs(v, num_list, s):
    global res
    if s > res:
        return
    else:
        for i in range(n - k + 1):
            for j in range(i, n - k + 1):
                tmp = reverse(num_list, j)
                if tmp not in visited:
                    visited[tmp] = min(s + 1, visited.get(num_list,987654321) + 1)
                    dfs(i, tmp, s + 1)


visited = {}
res = float('inf')
n, k = map(int, input().split())
numbers = input().replace(' ','')
sorted_numbers = ''.join(sorted(list(numbers)))
visited[numbers] = 0
dfs(0, numbers, 0)
print(visited.get(sorted_numbers,-1))
print(visited)


#
#
#
#
# from copy import deepcopy
# def reverse(li, s):
#     return li[:s] + li[s:s+k][::-1] + li[s+k:]
#
#
# def dfs(v, s, res):
#     global m
#     if sorted_numbers == res:
#         if m > s:
#             m = s
#         return
#     else:
#         for i in range(n - k + 1):
#             visited.append(deepcopy(reverse(res,i)))
#             dfs(i, s + 1, visited[-1])
#
# visited = []
# n, k = map(int, input().split())
# numbers = ''.join(list(input().split()))
# sorted_numbers = ''.join(sorted(numbers))
# m = float('inf')
# if sorted_numbers == numbers:
#     print(0)
# else:
#     dfs(0,[])

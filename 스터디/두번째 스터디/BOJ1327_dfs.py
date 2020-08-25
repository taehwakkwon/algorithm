import sys
sys.stdin = open('input.txt')

from copy import deepcopy
import sys
sys.setrecursionlimit(10**8)
def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n

def dfs(v, num_string, s):
    global res
    if visited.get(sorted_numbers,987654321) < s:
        return
    else:
        for i in range(n - k + 1):
            tmp = num_string[:i] + num_string[i:i+k][::-1] + num_string[i+k:]
            if tmp in visited:
                visited[tmp] = min(s + 1, visited[tmp])
                if s + 1 > visited[tmp]:
                    continue
                else:
                    visited[tmp] = s + 1
                dfs(i, tmp, s + 1)
            else:
                visited[tmp] = s + 1
                dfs(i, tmp, s + 1)

for n in range(2,9):
    for k in range(2,n):
        #n, k = map(int, input().split())
        print(n, k)
        numbers = ''.join(list(map(str, range(n,0,-1))))
        sorted_numbers = ''.join(sorted(numbers))
        visited = {}
        visited[numbers] = 0
        dfs(0, numbers, 0)
        print(visited.get(sorted_numbers, -1))
# print(visited.get(sorted_numbers,-1))
# print(visited, len(visited))

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

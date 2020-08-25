import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(10**8)
def dfs(num_string, s):
    global res
    if visited.get(sorted_numbers,987654321) < s or s > 30:
        return
    else:
        for i in range(n - k + 1):
            tmp = num_string[:i] + num_string[i:i+k][::-1] + num_string[i+k:]
            if tmp in visited:
                if s + 1 > visited[tmp]:
                    continue
                else:
                    visited[tmp] = s + 1
                dfs(tmp, s + 1)
            else:
                visited[tmp] = s + 1
                dfs(tmp, s + 1)


visited = {}
n, k = map(int, input().split())
numbers = input().replace(' ','')
sorted_numbers = ''.join(sorted(list(numbers)))
visited[numbers] = 0
dfs(numbers, 0)
print(visited.get(sorted_numbers, -1))
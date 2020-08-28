import sys
sys.stdin = open("sample_input.txt", "r")
sys.setrecursionlimit(10**7)
import time
def DP(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    elif arr[N] != 0:
        return arr[N]
    else:
        arr[N] = (DP(N-10) + DP(N-20) * 2)%1000000000
        return arr[N]
start = time.time()
for i in range(1):
    T = int(input())
    for tc in range(T):
        N = int(input())
        arr = [0]*(N+1)
        DP(N)
        print('#%d %d' % (tc+1, DP(N)))
print('time: ', (time.time()-start))
def DP(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    elif N != 0:
        return (DP(N-10) + DP(N-20) * 2)%1000000000

import time
start = time.time()

for i in range(1):
    T = int(input())
    for tc in range(T):
        N = int(input())
        DP(N)
        print('#%d %d' % (tc+1, DP(N)))

print('time: ', (time.time() - start))

'''
def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '{' or arr[i] == '[':  # push
            stack.append(arr[i])
        elif arr[i] == ')':  # pop하고 비교
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif arr[i] == '}':  # pop하고 비교
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif arr[i] == ']':  # pop하고 비교
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


T = int(input())
for tc in range(T):
    arr = input()
    stack = []
    print(check(arr))



def DFS(node):
    global res
    visited.append(node)
    if node == g:
        res = 1
        return
    else:
        for i in range(51):
            if arr[node][i] == 1 and i not in visited:
                DFS(i)

T = int(input())
for tc in range(1, T + 1):
    arr = [[0]*51 for _ in range(51)]
    V, E = map(int, input().split())
    for i in range(E):
        x, y = map(int, input().split())
        arr[x][y] = 1
    s, g = map(int, input().split())
    visited = []
    res = 0
    DFS(s)
    print('#%d %d' % (tc, res))


'''
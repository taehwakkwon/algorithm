import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs():
    queue = deque([])
    for i in range(1, v + 1):
        if i in dic and i not in check:
            queue.append(i)
    result = []
    while len(result) != v:
        s = queue.popleft()
        print(s, queue, check)
        if s not in check:
            result.append(s)
            for key in check:
                if s in check[key]:
                    check[key].remove(s)
                    break
            if key in check and check[key] == []:
                del check[key]
            queue.append(key)
        else:
            queue.append(s)
    print(*result)





T = 10
for t in range(1, T + 1):
    print('#%d ' %t, end = '')
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [0] * (v + 1)
    check = {}
    dic = {}

    for i in range(0, len(data),2):
        dic[data[i]] = dic.get(data[i], []) + [data[i + 1]]
        check[data[i + 1]] = dic.get(data[i + 1], []) + [data[i]]
    print()
    print(dic)
    print(check)
    bfs()


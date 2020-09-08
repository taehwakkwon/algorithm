import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T + 1):
    print('#%d ' %t, end = '')
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [0] * (v + 1)
    dic = {i: [] for i in range(1, v + 1)}
    total = 0
    for i in range(0, len(data),2):
        dic[data[i]] = dic.get(data[i], []) + [data[i + 1]]

    result = []
    while len(result) != v:
        for i in range(1, v + 1):
            if visited[i] == 0: #방문하지 않은곳
                for value in dic[i]:
                    if visited[value] == 0:
                        break
                else:
                    visited[i] = 1
                    result = [i] + result

    print(*result)


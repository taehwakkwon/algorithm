import sys
sys.stdin = open('../now/input.txt')

#두개의 선거구로 나눠
def check(v, visited, li):
    for value in dic[v]:
        if visited[value-1] == 0 and li[value-1] == 1:
            visited[value-1] = 1
            check(value, visited, li)


n = int(input())
populations = list(map(int, input().split()))
total = sum(populations)
min_val = total
dic = {i:[] for i in range(1,n+1)}

for i in range(n):
    infos = list(map(int, input().split()))
    for j in range(1, infos[0]+1):
        dic[i+1].append(infos[j])

base = (2**n) -1

for i in range(1, base):
    a_flag = b_flag = False
    a_pop = b_pop = 0
    a = [0]*n
    b = [0]*n
    asum = 0
    for j in range(n):
        if i & (1<<j):
            a[j] = 1
        else:
            b[j] = 1
    visited_a = [0]*n
    visited_b = [0]*n

    for j in range(n):
        if a[j] == 1:
            visited_a[j] = 1
            check(j+1, visited_a,a)
            break
    if visited_a != a:
        continue
    for j in range(n):
        if b[j] == 1:
            visited_b[j] = 1
            check(j+1,visited_b,b)
            break
    if visited_b != b:
        continue
    asum = 0
    for j in range(n):
        if a[j] == 1:
            asum += populations[j]
    min_val = min(min_val, abs((total-asum) - asum))
if min_val == total:
    print(-1)
else:
    print(min_val)
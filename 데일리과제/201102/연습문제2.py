def dfs(v,s,left):
    if s + left < 10:
        return
    if v == n:
        if s == 10:
            for i in range(n):
                if res[i] != 0:
                    print(res[i], end = ' ')
            print()
    else:
        res[v] = numbers[v]
        dfs(v + 1,s + numbers[v], left - numbers[v])
        res[v] = 0
        dfs(v + 1, s, left - numbers[v])


numbers = list(range(1,11))
n = len(numbers)
res = [0]*n
dfs(0,0,sum(numbers))
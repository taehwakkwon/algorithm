def solution(a):
    def dfs(v, flag):
        print(v)
        if v == 1:
            for i in range(n):
                if a[i] != 0:
                    dic[a[i]] = 0
            return
        else:
            for i in range(n - 1):
                if type(a[i]) == int:
                    for j in range(i + 1, n):
                        if type(a[j]) == int:
                            print(a[i],a[j])
                            if a[i] < a[j]:
                                tmp = a[i]
                                a[i] = 'x'
                                dfs(v - 1, flag)
                                a[i] = tmp
                            elif a[i] > a[j]:
                                tmp = a[j]
                                a[i] = 'x'
                                dfs(v - 1, flag)
                                a[j] = tmp
                            elif flag == True and a[i] > a[j]:
                                tmp = a[i]
                                a[i] = 'x'
                                dfs(v - 1, False)
                                a[i] = tmp
    n = len(a)
    dic = {}
    dfs(n, True)
    print(dic)

    return len(dic)

print(solution([9,-1,-5]))
#solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
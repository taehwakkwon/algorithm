def solution(a):
    global cnt
    cnt = 0
    n = len(a)
    def boom(v, flag):
        global cnt
        if v == 1:
            for i in range(n):
                if type(a[i]) == int:
                    last.add(a[i])
                    break
        else:
            for i in range(n):
                if type(a[i]) == int:
                    for j in range(i + 1, n):
                        if type(a[j]) == int:
                            if a[i] < a[j]:
                                x = a[i]
                                a[i] = 'x'
                                boom(v - 1, flag)
                                a[i] = x
                                if flag:
                                    y = a[j]
                                    a[j] = 'x'
                                    boom(v - 1, False)
                                    a[j] = y


                            if a[i] > a[j]:
                                z = a[j]
                                a[j] = 'x'
                                boom(v - 1, flag)
                                a[j] = z
                                if flag:
                                    w = a[i]
                                    a[i] = 'x'
                                    boom(v - 1, False)
                                    a[i] = w

    last = set([])
    boom(n, True)
    return len(last)

print(solution([9,-1,-5]))
#solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
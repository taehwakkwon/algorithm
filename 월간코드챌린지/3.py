def solution(a):
    global cnt
    cnt = 0
    n = len(a)
    def boom(v, flag, targit):
        if v == 1:
            if sum(check) == 1:
                last.add(targit)
                return 
        else:
            for i in range(n):
                if check[i] == 1:
                    for j in range(i + 1, n):
                        if check[j] == 1:
                            if a[i] < a[j]:
                                if j != targit:
                                    check[j] = 0
                                    boom(v - 1, flag, targit)
                                    check[j] = 1
                                else:
                                    check[i] = 0
                                    boom(v - 1, False, targit)
                                    check[i] = 1
                            else:
                                if i != targit:
                                    check[i] = 0
                                    boom(v - 1, flag, targit)
                                    check[i] = 1
                                else:
                                    check[j] = 0
                                    boom(v - 1, False, targit)
                                    check[j] = 1




    last = set([])
    for i in range(n):
        check = [1]*(n)
        boom(n, True, i)
    return len(last)

#print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
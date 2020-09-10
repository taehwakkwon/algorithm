def solution(a):
    n = len(a)
    if n <= 2:
        return n
    cnt = 2
    for i in range(1, n - 1):
        tmp = 0
        pre_a = float('inf')
        pre_b = float('inf')

        for j in range(i + 1):
            if a[i] > a[j] or a[i] > pre_a:
                tmp += 1
                pre_a = min(a[j], pre_a)
                break
        for j in range(i + 1, n):
            if a[i] > a[j] or a[i] > pre_b:
                tmp += 1
                pre_b = min(a[j], pre_b)
                break
        if tmp < 2:
            cnt += 1
    return cnt




print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))









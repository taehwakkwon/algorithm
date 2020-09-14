import sys
import time
def solution(orders, course):
    def combinations(v, s, m, res):
        if v == m:
            for i in range(len(orders)):
                for j in range(m):
                    if res[j] not in orders[i]:
                        break
                else:
                    tmp = ''.join(sorted(list(res)))
                    dic_result[tmp] = dic_result.get(tmp, 0) + 1
        else:
            for i in range(s, len(dic_keys)):
                combinations(v + 1, i + 1, m, res + dic_keys[i])

    dic_keys = set([])
    for i in range(len(orders)):
        for j in range(len(orders[i])):
            dic_keys.add(orders[i][j])
    dic_keys = list(dic_keys)
    result = []
    for m in range(2,len(dic_keys)):
        res = ''
        dic_result = {}
        combinations(0,0,m, res)
        result.append(sorted(dic_result.items(), key = lambda x: x[1], reverse = True))
    ans = []
    for cor in course:
        M = 2
        for i in range(len(result[cor-2])):
            if M <= result[cor-2][i][1]:
                M = result[cor-2][i][1]
                ans.append(result[cor-2][i][0])
            else:
                break
    print(time.time() - start)
    return sorted(ans)


#2ms
#0.46
start = time.time()
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH","ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD","XYZ", "XWY", "WXA"],[2,3,4,5]))
start = time.time()
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
start = time.time()
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
start = time.time()
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

# from itertools import combinations
# a = list(combinations(list(map(chr, range(ord('A'),ord('A')+20))), 10))
# print(a)
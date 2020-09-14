import sys

from itertools import combinations
def solution(orders, course):
    len_list = list(map(len, orders))
    result = []
    for cor in course:
        dic = {}
        for j in range(len(orders)):
            tmp = list(combinations(orders[j], cor))
            for k in range(len(tmp)):
                dic[''.join(sorted(list(tmp[k])))] = 0
        result.append(dic)
    for i in range(len(result)):
        for key in result[i]:
            for order in orders:
                for j in key:
                    if j not in order:
                        break
                else:
                    result[i][key] += 1
        result[i] = sorted(result[i].items(), key = lambda x:x[1], reverse=True)
    while len(result) <= len(course):
        result.append([])
    ans = []
    for cor in range(len(course)):
        M = 2
        for i in range(len(result[cor])):
            if M <= result[cor][i][1]:
                M = result[cor][i][1]
                ans.append(result[cor][i][0])
    return sorted(ans)
    # print(orders)
    # print(comb[0])
    # print(comb[1])
    # print(comb[2])
    #print(time.time() - start)



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
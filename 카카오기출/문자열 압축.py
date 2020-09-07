def solution(s):
    res = []
    answer = []
    if len(s) <= 2:
        return len(s)
    for i in range(1, len(s) // 2 + 1):
        string, num = '', 1
        for j in range(i, len(s), i):
            pre = s[j - i:j]
            now = s[j: j + i]
            if pre == now:
                num += 1
            else:
                if num == 1:
                    string += pre
                else:
                    string += str(num) + pre
                    num = 1
        else:
            if num != 1:
                string += str(num) + now
            else:
                string += now

        res.append(string)
        answer.append(len(res[-1]))

    return min(answer)
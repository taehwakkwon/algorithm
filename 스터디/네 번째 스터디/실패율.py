def solution(N, stages):
    dic = {i : 0 for i in range(1, N + 2)}
    n = len(stages)
    stages = sorted(stages)
    for i in range(len(stages)):
        if dic[stages[i]] == 0:
            dic[stages[i]] = stages.count(stages[i])/(n - i)
    return [x[0] for x in sorted(dic.items(), key = lambda x : x[1], reverse = True) if not x[0] == N + 1]
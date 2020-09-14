#개발언어 직군 경력 소울프드 코테점수
import sys


def solution(info, query):
    cpp, java, python = set([]), set([]), set([])
    backend, frontend = set([]), set([])
    junior, senior = set([]), set([])
    chicken, pizza = set([]), set([])
    score = []
    score_dic = {}
    tmp = []
    for i in query:
        tmp.append(int(i.split()[-1]))
    tmp.sort()
    score_dic = {}
    for i in tmp:
        score_dic[i] = []
    for i, line in enumerate(info):
        line = line.split()
        if line[0] == 'cpp':
            cpp.add(i)
        elif line[0] == 'java':
            java.add(i)
        elif line[0] == 'python':
            python.add(i)

        if line[1] == 'backend':
            backend.add(i)
        elif line[1] == 'frontend':
            frontend.add(i)

        if line[2] == 'junior':
            junior.add(i)
        elif line[2] == 'senior':
            senior.add(i)

        if line[3] == 'chicken':
            chicken.add(i)
        elif line[3] == 'pizza':
            pizza.add(i)
        for key in score_dic:
            if int(line[4]) >= key:
                score_dic[key].append(i)
            else:
                break
    result = []
    for line in query:
        line = line.replace('and', '').split()

        s = set(list(range(len(info))))
        if line[2] == 'junior':
            s &= junior
        elif line[2] == 'senior':
            s &= senior

        if line[4].isnumeric():
            s &= set(score_dic[int(line[4])])

        if line[3] == 'chicken':
            s &= chicken
        elif line[3] == 'pizza':
            s &= pizza

        if line[0] == 'java':
            s &= java
        elif line[0] == 'cpp':
            s &= cpp
        elif line[0] == 'python':
            s &= python
        if line[1] == 'backend':
            s &= backend
        elif line[1] == 'frontend':
            s &= frontend




        result.append(len(s))
    return result
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
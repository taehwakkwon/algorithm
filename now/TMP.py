import sys
sys.stdin=open('input.txt')

import time
start = time.time()


def solution(genres, plays):
    dic_total = {}
    dic = {}
    for idx, genre, play in zip(range(len(plays)), genres, plays):

        if genre in dic:
            dic[genre].append((play, idx))
            dic_total[genre] += play
        else:
            dic[genre] = [(play, idx)]
            dic_total[genre] = play

    dic_total = sorted(dic_total.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for key, value in dic_total:
        dic[key] = sorted(dic[key],key=lambda x:[-x[0],x[1]])
        jdx = 0
        for play, idx in dic[key]:
            if jdx > 1:
                break
            jdx += 1
            answer.append(idx)
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(time.time()-start)
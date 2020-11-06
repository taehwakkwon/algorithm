def solution(s):
    #0제거
    #길이를 2진법으로 변환
    cnt = 0
    delete = 0
    while s != '1':
        bf = len(s)
        s = s.replace('0','')
        delete += (bf-len(s))
        cnt += 1
        s = bin(len(s))[2:]

    return [cnt, delete]

print(solution("110010101001"))
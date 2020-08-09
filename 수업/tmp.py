import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = []
    for num in range(9):
        numbers = list(map(int, input().split()))
        arr.append(numbers)
        result = 0
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] == numbers[j]:
                    result = 0
                else:
                    result = 1




T = int(input())
for tc in range(1, T+1):
    S = list(map(int,input().split()))
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    S_li = []
    for _ in range(S):
        S_li.append(list(map(int, input().split())))

    for i in range(len(S_li)):
        m = []
        for k in range(len(S_li[i])):
            m.append(S_li[i][k])
            if m.sort()!= A:
                result = 0
                break
            else :
                for j in range(len(S_li[0])):
                    p = []
                    for h in range(len(S_li)):
                        p.append(S_li[j][h])
                        if p.sort() != A:
                            result = 0
                            break
                        else :
                            for a in range(0, 9, 3):
                                u = []
                                for b in range(0, 9, 3):
                                    u.append(S_li[a][b])
                                    if u.sort() != A:
                                        result =0
                                        break
                                    else:
                                        result = 1

    print(result)
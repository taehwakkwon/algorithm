def solution(n):
    answer = []
    mat = []
    for i in range(n):
        row = [0 for _ in range(i+1)]
        mat.append(row)

    goal = calc(n)
    val = 1
    mode = 0
    col = 0
    row = 0
    flag = False
    while(True):
        if mode == 0:
            for i in range(n):
                mat[row+i][col] = val
                if val == goal:
                    flag = True
                    break
                val += 1
            row = row+i
            col += 1
            n -= 1
            mode = 1
        elif mode == 1:
            for i in range(n):
                mat[row][col+i] = val
                if val == goal:
                    flag = True
                    break
                val += 1
            col = col + i
            n -= 1
            mode = 2
        else:
            for i in range(n):
                mat[row-i-1][col-i-1] = val
                if val == goal:
                    flag = True
                    break
                val += 1
            row = row-i
            col = col-i-1
            n -= 1
            mode = 0
        if flag == True:
            break
    for i in mat:
        for j in i:
            answer.append(j)
    return answer


def calc(n):
    if n == 4:
        return 10
    else:
        return n+calc(n-1)


print(solution(1000))
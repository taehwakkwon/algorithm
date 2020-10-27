code_index = ['3211', '2221', '2122', '1411', '1132',
              '1231', '1114', '1312', '1213', '3112']


def binaryarr():
    for i in range(N):
        binay_num = bin(int(board[i], 16))[2:]
        temp = (len(str(board[i])) - 2) * 4 - len(binay_num)
        binay_num = '0' * temp + binay_num
        board[i] = binay_num


def check(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == '1':
            end = i
            break
    while end >= 0:
        code = ''
        for _ in range(8):
            c1, c2, c3, c4 = 0, 0, 0, 0
            while arr[end] == '1':
                c4, end = c4 + 1, end - 1
            while arr[end] == '0':
                c3, end = c3 + 1, end - 1
            while arr[end] == '1':
                c2, end = c2 + 1, end - 1
            while arr[end] == '0':
                end = end - 1
            m = min(c2, c3, c4)
            c1 = 7 - sum([c2 // m, c3 // m, c4 // m])
            str_temp = ''.join([str(c1), str(c2 // m), str(c3 // m), str(c4 // m)])
            code_int = code_index.index(str_temp)
            code += str(code_int)
        code_list.add(''.join(list(reversed(code))))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    binaryarr()
    code_list = set()
    for b in board:
        if '1' in b:
            check(b)

    result = []
    for c in list(code_list):
        res = 0
        for i in range(8):
            if i % 2 == 0:
                res += int(c[i]) * 3
            else:
                res += int(c[i])

        if (res % 10) == 0:
            temp2 = 0
            for cc in c:
                temp2 += int(cc)
            result.append(temp2)
        else:
            result.append(0)
    print('#{} {}'.format(tc, sum(result)))
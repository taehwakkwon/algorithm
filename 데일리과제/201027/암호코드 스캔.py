import sys
sys.stdin = open('input.txt')

hex_dic = {}
for key, value in zip(list(map(str,range(10))) + list(map(chr,range(ord('A'),ord('A')+6))), range(16)):
    tmp = list(map(int,bin(value)[2:]))
    hex_dic[key] = [0]*(4-len(tmp)) + tmp
code = {(2,1,1):0, (2,2,1):1, (1,2,2):2, (4,1,1):3, (1,3,2):4,
        (2,3,1):5, (1,1,4):6, (3,1,2):7, (2,1,3):8, (1,1,2):9}

def solve():
    result = 0
    for i in range(n):
        #뒷쪽에서부터 검사
        j = m * 4 - 1
        while j >= 55:
            #만약에 1을 찾았는데, 위쪽도 같이 1이면, 암호 첫번째 줄이 아님
            #검사를 할 필요가 없음
            pwd = []
            if arr[i][j] and arr[i-1][j] == 0: #암호 코드의 첫번째 줄 시작
                #암호코드 해독 시작
                for _ in range(8):
                    n2 = n3 = n4 = 0
                    while arr[i][j] == 0:
                        j -= 1
                    while arr[i][j] == 1:
                        n4 += 1
                        j -= 1
                    while arr[i][j] == 0:
                        n3 += 1
                        j -= 1
                    while arr[i][j] == 1:
                        n2 += 1
                        j -= 1

                    min_v = min(n2,n3,n4)
                    c = (n2/min_v,n3/min_v,n4/min_v)
                    pwd.append(code[c])
                sum_even = sum(pwd[2::2])
                sum_odd = sum(pwd[1::2])
                tmp = sum_odd*3 + sum_even + pwd[0]
                if tmp%10 == 0:
                    result += sum(pwd)
            j -= 1
    return result

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        tmp_arr = []
        tmp = input()
        for j in range(m):
            tmp_arr += hex_dic[tmp[j]]
        arr.append(tmp_arr)
    result = solve()
    print('#%d %d' %(t,result))

import sys
sys. stdin = open("sample_input.txt", "r")

str1_num = []

T = int(input())
for tc in range(T):
    str1_num = []
    str1 = list(input())
    for new in range(1, len(str1)+1):
        new = 0
        str1_num.append(new)

    list_C = { name:value for name, value in zip(str1,str1_num)}
    print(list_C.keys())

    str2 = list(input())
    count = 0
    for x in str2:
        if x == list_C.keys():
            list_C += 1
        print(list_C)
    #     print(str2)
        # if x == ''
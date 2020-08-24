# import sys
# sys.stdin = open('sample_input.txt')
def sort(li):
    dic = {}
    for num in number_list:
        dic[num] = 0
    for num in li:
        dic[num] += 1
    for num in number_list:
        while dic[num]:
            print(num, end = ' ')
            dic[num] -= 1

number_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for i in range(T):
    t, num_len = input().split()
    num_len = int(num_len)
    numbers = list(input().split())
    print(t)
    sort(numbers)



import sys
sys. stdin = open("sample_input.txt", "r")

T = int(input())
for i in range(T):
    a, b = input().split()
    b = int(b)
    ZRO = 0
    ONE = 0
    TWO = 0
    THR = 0
    FOR = 0
    FIV = 0
    SIX = 0
    SVN = 0
    EGT = 0
    NIN = 0
    num_list = list(map(str, input().split()))
    for j in range(b):
        if num_list[j] == 'ZRO':
            ZRO += 1
        elif num_list[j] == 'ONE':
            ONE += 1
        elif num_list[j] == 'TWO':
            TWO += 1
        elif num_list[j] == 'THR':
            THR += 1
        elif num_list[j] == 'FOR':
            FOR += 1
        elif num_list[j] == 'FIV':
            FIV += 1
        elif num_list[j] == 'SIX':
            SIX += 1
        elif num_list[j] == 'SVN':
            SVN += 1
        elif num_list[j] == 'EGT':
            EGT += 1
        else:
            NIN += 1


#!/bin/python3

import math
import os
import random
import re
import sys

sys.stdin = open('input.txt')
#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    path = list(path)
    dic = {'U':'/','D':'\\'}

    loc = [(0, 0, '_')]
    height = 0
    M, m = 0, float('inf')
    for i in range(len(path)):
        M = max(M, height)
        m = min(m, height)
        if path[i] == 'D':
            height -= 1
            loc.append((loc[-1][0] + 1, height, dic[path[i]]))
        elif path[i] == 'U':
            loc.append((loc[-1][0] + 1, height, dic[path[i]]))
            height += 1

    loc.append((len(path)+1,height,'_'))
    mountain = [['']*(len(path) + 2) for _ in range(M+abs(m) + 1)]
    res = ''

    for x, y, oper in loc:
        mountain[M-y][x] = oper

    for i in range(1,len(mountain)):
        for j in range(len(mountain[i])):
            if mountain[i][j] == '':
                res += ' '
            else:
                res += mountain[i][j]
        res += '\n'

    return res

    # Write your code here


if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)



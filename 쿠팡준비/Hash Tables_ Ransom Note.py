#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine = magazine.split()
    note = note.split()
    idx = len(note) - 1
    for word in magazine[::-1]:
        if word == note[idx]:
            note.pop()
    if note:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

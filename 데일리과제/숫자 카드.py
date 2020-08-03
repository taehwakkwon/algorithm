import sys
sys.stdin = open('sample_input.txt')

import sys


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        cards = list(map(int, input()))
        dic = {}
        for card in cards:
            dic[card] = dic.get(card, 0) + 1
        dic = sorted(dic.items(), key = lambda x:[x[1],x[0]], reverse = True)
        print('#%d %d %d' %(i+1, dic[0][0], dic[0][1]))
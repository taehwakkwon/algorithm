import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, 1 + T):
    cards = {'S': [], 'D': [], 'H': [], 'C': []}
    num = loc = ''
    res = ''

    for string in input():
        if string in cards:
            if loc:
                if int(num) in cards[loc]:
                    res = 'ERROR'
                    break
                cards[loc].append(int(num))
                num = ''
            loc = string
        elif string.isdigit():
            num += string
    else:
        if int(num) in cards[loc]:
            res = 'ERROR'
        cards[loc].append(int(num))
    ans = [13]*4
    for i, key in enumerate(['S','D','H','C']):
        ans[i] -= len(cards[key])
    if res:
        print('#%d ERROR' %t)
    else:
        print('#%d' %t, *ans)
#import sys
#sys.stdin = open('sample_input.txt')
def win(left, right):
    a, b = cards[left], cards[right]
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2) or a == b:
        return left
    return right


def div_con(left, right):
    global cards
    if left == right:
        return left

    start = div_con(left, (left + right)//2)
    end = div_con((left + right)//2 + 1, right)
    return win(start, end)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input().split()))
    print('#%d %d' %(t, div_con(0, n - 1) + 1))

#import sys
#sys.stdin = open('sample_input.txt')

def min_max(number_list):
    M = 0
    m = float('inf')
    for number in number_list:
        if M < number:
            M = number
        if m > number:
            m = number
    return M, m


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        numbers = list(map(int, input().split()))
        M, m = min_max(numbers)
        print('#%d %d' %(i + 1, M - m))




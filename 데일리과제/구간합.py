import sys
sys.stdin = open('sample_input.txt')

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        numbers = list(map(int, input().split()))
        dp_numbers = [0]
        for num in numbers:
            dp_numbers.append(num + dp_numbers[-1])
        mn = dp_numbers[-1]
        M = 0
        diff = 0
        for j in range(m,len(dp_numbers)):
            diff = dp_numbers[j] - dp_numbers[j-m]
            if mn > diff:
                mn = diff
            if M < diff:
                M = diff
        print('#%d %d' %(i + 1, M - mn))
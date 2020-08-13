import sys
sys.stdin = open('sample_input.txt')
def binary_search(find):
    right = p
    left = 1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        if mid == find:
            return cnt
        elif mid > find:
            right = mid
        else:
            left = mid

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        p, a, b = map(int,input().split())
        cnt_a = binary_search(a)
        cnt_b = binary_search(b)
        if cnt_a == cnt_b:
            res = '0'
        elif cnt_a > cnt_b:
            res = 'B'
        else:
            res = 'A'
        print('#%d %s' %(t, res))


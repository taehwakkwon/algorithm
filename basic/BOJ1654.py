import sys
sys.stdin = open('input.txt','r')

def count(len):
    cnt = 0
    for x in lines:
        cnt += x//len
    return cnt

if __name__ == "__main__":
    k,n = map(int, input().split())
    lines = sorted([int(input()) for _ in range(k)])
    left = 1
    right = lines[-1]
    while left <= right:
        mid = (left+right)//2
        if count(mid) >= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    print(res)

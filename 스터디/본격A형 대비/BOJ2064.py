import sys
sys.stdin = open('input.txt')


n = int(input())
for t in range(n):
    ip = list(map(bin, map(int, input().split('.'))))
    print(ip)
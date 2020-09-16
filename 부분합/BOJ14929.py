import sys
sys.stdin = open('input.txt')
n = int(input())
x = list(map(int,input().split()))
s = [0]
for i in range(n):
    s.append(x[i]+s[-1])
sig = 0

for i in range(len(x)):
    sig += x[i]*(s[n]-s[i+1])
print(sig)
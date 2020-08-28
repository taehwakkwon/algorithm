import sys
sys.stdin = open("sample_input.txt", "r")
sys.setrecursionlimit(10**7)
def DP(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    elif N != 0:
        return (DP(N-10) + DP(N-20) * 2)%1000000000


import time
start = time.time()

for i in range(1):
    T = int(input())
    for tc in range(T):
        N = int(input())
        DP(N)
        print('#%d %d' % (tc+1, DP(N)))

print('time: ', (time.time() - start))

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for t in range(1, T+1):
    N = input()
    M = input()
    for i in range(len(M)-len(N)+1):
        if M[i:i+len(N)] == N:
            print('#%d %d' %(t, 1))
            break
    else:
        print('#%d %d' % (t, 0))

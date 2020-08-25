import sys
sys.stdin=open('sample_input.txt')
T = int(input())
for t in range(1, T + 1):
    N = input()
    M = input()
    dic = {}
    for i in range(len(N)):
        dic[N[i]] = 0
    for i in range(len(M)):
        if M[i] in dic:
            dic[M[i]] += 1
    print('#%d %d' %(t, sorted(dic.items(), key=lambda x:x[1], reverse = True)[0][1]))
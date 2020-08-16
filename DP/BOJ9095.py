import sys
sys.stdin = open('input.txt','r')
def dynamic(n):
    global dp
    if n < 0: return 0
    if n <= 1: return 1
    if dp[n]: return dp[n]
    dp[n] = dynamic(n-1) + dynamic(n-2) + dynamic(n - 3)
    return dp[n]

if __name__ == "__main__":
    t = int(input())
    dp = [0]*12
    for i in range(t):
        print(dynamic(int(input())))


'''
0: 1
1: 1
2: 1    1, 2
3: 3
4: 7
5: 15
6: 
7: 44
8:
9:
10: 274

1 1 1 1 1:1
2 1 1 1:4 + 1
3 1 1:3 + 1
4 1:2 + 1

5 1: + 1

2 2 1:3// 2 2 1 1 6
3 2: 2// 3 2 1 6

3 3 : 1
4 2 : 2

2//
1 1

3//
1 1 1
1 2 : 2

4//
1 1 1 1
1 1 2: 3
2 2: 1
1 3: 2






'''

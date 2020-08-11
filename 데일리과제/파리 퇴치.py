import sys
sys.stdin = open('sample_input.txt')

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        n, m = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        M = 0
        for i in range(n - m + 1):
            for j in range(n - m + 1):
                tmp = 0
                for k in range(m):
                    for l in range(m):
                        tmp += board[i + k][j + l]
                if M < tmp:
                    M = tmp
        print('#%d %d' %(t,M))





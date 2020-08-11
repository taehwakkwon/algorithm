import sys
sys.stdin = open('sample_input.txt','r')

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        board_red = [[0]*10 for _ in range(10)]
        board_blue = [[0]*10 for _ in range(10)]

        for i in range(n):
            r1, c1, r2, c2, c = map(int, input().split())
            for j in range(r1, r2+1):
                for k in range(c1, c2+1):
                    if c == 1:
                        board_red[j][k] = 1
                    else:
                        board_blue[j][k] = 1
        cnt = 0
        for j in range(10):
            for k in range(10):
                if board_blue[j][k] and board_red[j][k]:
                    cnt += 1
        print('#%d %d' %(t, cnt))



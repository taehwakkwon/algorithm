import sys
sys.stdin = open('input.txt','r')


if __name__ == "__main__":
    r,c,m = map(int, input().split())
    board = [[]*c for _ in range(r)]
    for i in range(m):
        r,c,s,d,z = map(int, input().split())
        board[r-1][c-1].append(z)
        
    infos = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

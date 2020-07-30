import sys
sys.stdin = open('input.txt','r')

def z_recur(n):
    if n == 0:
        return
    else:
        for dy, dx in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            x = 2**(n-1) + 
            z_recur(n-1)




if __name__ == "__main__":
    N,r,c = map(int,input().split())
    y, x = 0, 0
    cnt = -1
    z_recur(N)
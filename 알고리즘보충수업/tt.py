import sys
sys.stdin=open('input.txt')

#import sys
import copy
#sys.stdin = open("sample_input.txt", "r")
#25분 시작

def combinations(L,s,numbers):
    if L == k:
        comb.append(copy.deepcopy(res))
    else:
        for i in range(s,len(numbers)):
            res[L] = numbers[i]
            combinations(L+1,i+1,numbers)

if __name__ == "__main__":
    T = int(input())
    ans = [0]*T
    for i in range(T):
        N = int(input())
        cells = [0]*N
        for j in range(N):
            cells[j] = list(map(int, input().split()))
        for j in range(N-1):
            for l in range(j+1,N):
                cells[j][l] += cells[l][j]
                cells[l][j] = 0
        res = [0]*(N//2)
        k = N//2
        comb = []
        combinations(0,0,list(range(N)))
        comb_A = comb[:len(comb)//2]
        comb_B = sorted(comb[len(comb)//2:],reverse = True)
        m = 2147000000
        for j,l in zip(comb_A,comb_B):
            k = 2
            res = [0]*k
            comb =[]
            combinations(0, 0, j)
            comba = comb

            comb = []
            combinations(0, 0, l)
            combb = comb

            A = 0
            B = 0
            print(comba,combb)
            for p,q in zip(comba, combb):
                A += cells[p[0]][p[1]]
                B += cells[q[0]][q[1]]
            if abs(A-B) < m:
                m = abs(A-B)
        ans[i] = m

    for i in range(T):
        print("#%d %d" %(i+1, ans[i]))
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    input_li = list(map(int, input().split()))
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)

    for i in range(0, E * 2, 2):
        p, c = input_li[i], input_li[i + 1]
        if L[p]:
            R[p] = c
        else:
            L[p] = c
        P[c] = p
    print(L)
    break
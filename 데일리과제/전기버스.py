import sys
sys.stdin = open('sample_input.txt')

def dfs(v, s, cnt):
    global M
    if v > len(bus_stops):
        if M > cnt:
            M = cnt
        return
    if s < 0:
        return
    else:
        if v in bus_stops:
            dfs(v + 1, k, cnt + 1)
            dfs(v + 1, s - 1, cnt)
        else:
            dfs(v + 1, s - 1, cnt + 1)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        k, n, m = map(int, input().split())
        bus_stops = list(map(int, input().split()))
        M = n
        dfs(0, k, 0)
        print(M)
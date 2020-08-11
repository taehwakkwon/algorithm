import sys
sys.stdin = open('sample_input.txt')

def dfs(v, s):
    global cnt
    if s > N:
        return
    if v > 12:
        if s != N:
            return
        total = 0
        for i in range(1,len(ch)):
            if ch[i]:
                total += i
        if total == K:
            cnt += 1
    else:
        dfs(v + 1, s)
        ch[v] = 1
        dfs(v + 1, s + 1)
        ch[v] = 0

if __name__ == "__main__":
    A = list(range(1,13))
    T = int(input())
    for t in range(1,T+1):
        N, K = map(int, input().split())
        ch = [0] * 13
        cnt = 0
        dfs(1, 0)
        print('#%d %d' %(t, cnt))














'''
def dfs(v,s):
    global cnt
    if s == N:
        total = 0
        for i in range(len(ch)):
            if ch[i]:
                total += i
        if total == K and ch not in res:
            res.append(ch)
            print(res)
    if v > 12 or s > N:
        return
    else:
        ch[v] = 1
        dfs(v + 1, s + 1)
        ch[v] = 0
        dfs(v + 1, s)

if __name__ == "__main__":
    A = list(range(1,13))
    T = int(input())
    for t in range(1,T+1):
        N, K = map(int, input().split())
        ch = [0] * 13
        res = []
        dfs(1, 0)
        print('#%d %d' %(t, len(res)))

'''
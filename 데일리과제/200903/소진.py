import sys
sys.stdin = open("input.txt", "r")
t = int(input())
for tc in range(1, t+1):
    n,m = map(int,input().split())
    ch = list(map(int,input().split()))
    queue = [0]*n
    # queue_2 = [i for i in range(m)]
    # print(visited)
    for i in range(n):
        queue[i] = ch[i]
    ch = ch[n:]
    for i in range(1000):

        a = queue[0]//2
        if queue.count(0) == n - 1:
            break

        if ch and queue[0]//2 == 0:
            queue.pop(0)
            queue.append(ch.pop(0))
        else :
            queue.pop(0)
            queue.append(a)
    print(queue, ch)
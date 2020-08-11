from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print_numbers = deque(list(map(int, input().split())))
    ch = deque([0] * len(print_numbers))
    ch[m] = 1
    idx = 0
    cnt = 0
    while True:
        M = max(print_numbers)
        if M == print_numbers[0]:
            print_numbers.popleft()
            cnt += 1
            if ch.popleft() == 1:
                print(cnt)
                break
        else:
            print_numbers.rotate(-1)
            ch.rotate(-1)
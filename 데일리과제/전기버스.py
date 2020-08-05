import sys
sys.stdin = open('sample_input.txt')

def can_go(v):
    global cnt, now
    while v < len(bus_stops) -1:
        if bus_stops[v] - now > k:
            print('#%d %d' % (t, 0))
            return
        else:
            if bus_stops[v + 1] - now > k:
                now = bus_stops[v]
                cnt += 1
                v += 1
            else:
                v += 1
    print('#%d %d' % (t, cnt))
    return


if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        k, n, m = map(int ,input().split())
        bus_stops = list(map(int ,input().split()))
        bus_stops.append(n)
        now,cnt = 0, 0
        can_go(0)
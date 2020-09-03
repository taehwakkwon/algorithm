import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node_list = [input().split() for _ in range(E)]
    S, G = map(int, input().split())
    queue = []
    r = 0
    c = 0
    print(node_list)
    for i in range(E):
        node_list[i][0]
        r, c = i, 0
        queue.append((r, c))
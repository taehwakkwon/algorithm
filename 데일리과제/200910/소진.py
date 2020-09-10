import sys
sys.stdin = open("input.txt", "r")

def binary(node):
    global cnt
    #배열크기 지정(N=노드크기)
    if node <= N:
        #왼쪽노드는 현재 인덱스의 2배
        binary(node*2)
        #더이상 못가면 값을 넣자
        print(node)
        tree[node] = cnt
        #값을 넣었을 때 증가시키기
        cnt += 1
        #우측 노드는 인덱스의 2배 + 1
        binary(node*2+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1
    binary(1)
    print(tree)
    print('#%d' %tc, tree[1], tree[N//2])
    break
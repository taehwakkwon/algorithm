import sys
sys.stdin = open('input.txt')


#중간 앞
def binary_tree(v):
    global cnt
    if v > n:
        return
    else:
        binary_tree(2 * v)
        tree[v] = cnt
        print(v)
        cnt += 1
        binary_tree(2*v + 1)



T = int(input())
for t in range(1, T + 1):
    n = int(input())
    tree = [0]*(n+1)
    cnt = 1
    binary_tree(1)
    print('#%d %d %d' %(t, tree[1], tree[n//2]))
    break


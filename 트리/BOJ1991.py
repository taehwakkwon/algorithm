import sys
sys.stdin = open('input.txt')

def pre_order(v):
    if v == '.':
        return
    else:
        print(v, end = '')
        if v in tree:
            for value in tree[v]:
                if value == '.':
                    continue
                pre_order(value)

def mid_order(v):
    if v == '.':
        return
    else:

        if v in tree:
            mid_order(tree[v][0])
            print(v, end='')
            mid_order(tree[v][1])

def post_order(v):
    if v == '.':
        return
    else:
        if v in tree:
            for value in tree[v]:
                if value == '.':
                    continue
                post_order(value)
            print(v, end='')

n = int(input())
tree = {}
for i in range(n):
    a, b, c  = input().rstrip().split()
    tree[a] = [b,c]
pre_order('A')
print()
mid_order('A')
print()
post_order('A')

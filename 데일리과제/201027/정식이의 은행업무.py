import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    binary = list(map(int, input()))
    ternary = list(map(int, input()))
    binarys = []
    ternarys = []
    for i in range(len(binary)):
        tmp = binary[:]
        tmp[i] = binary[i] ^ 1
        binarys.append(int(''.join(map(str,tmp)), base=2))
    for i in range(len(ternary)):
        tmp = ternary[:]
        for j in range(3):
            if tmp[i] == str(j):
                continue
            ternarys.append(int(''.join(map(str,tmp[:i]+[str(j)]+tmp[i+1:])), base=3))
    ans = set(binarys) & set(ternarys)
    print('#%d %s' %(t, *ans))

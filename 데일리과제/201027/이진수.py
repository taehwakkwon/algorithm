
numbers = list(map(str,range(10))) + list(map(chr,range(ord('A'),ord('A')+6)))
def hexa_to_binary(number):
    ans = ''
    for num in number:
        num = numbers.index(num)
        tmp = ''
        while num or len(tmp) < 4:
            tmp += str(num%2)
            num //= 2
        ans += tmp[::-1]
    return ans

T = int(input())
for t in range(1, T+1):
    a, b = input().split()
    print('#%d %s' %(t, hexa_to_binary(b)))

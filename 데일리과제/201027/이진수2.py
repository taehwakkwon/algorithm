import sys
sys.stdin = open('input.txt')
def change_system(number):
    ans = ''
    for i in range(1,13):
        d = 2**(-i)
        if number == 0:
            break
        if number >= d:
            number -= d
            ans += '1'
        else:
            ans += '0'
    if number:
        return 'overflow'
    else:
        return ans

T = int(input())
for t in range(1, T+1):
    number = float(input())
    print('#%d %s' %(t, change_system(number)))

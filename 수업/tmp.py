import sys
sys.stdin = open('input.txt')

def BubbleSort(a) :
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a #값 리턴

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    list_s = list(map(int, input().split()))
    list_s = BubbleSort(list_s)

    zero_list = [0] * 10
    list_front = list_s[0:len(list_s)//2]
    list_back = list_s[len(list_s)//2:]
    list_back_reverse = list_back[::-1]
    for h in range(len(zero_list)//2):
        zero_list[2*h] = list_back_reverse[h]
        zero_list[2*h+1] = list_front[h]
    print('#%d %s' %(tc, ' '.join(map(str,zero_list))))
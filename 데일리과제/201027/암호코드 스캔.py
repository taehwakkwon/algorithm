import sys
sys.stdin = open('input.txt')
dic = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}
numbers = list(map(str,range(10))) + list(map(chr,range(ord('A'),ord('A')+6)))
def hexa_to_binary(number):
    print(number)
    div = len(number)//15
    ans = ''
    for num in number:
        num = numbers.index(num)
        tmp = ''
        while num or len(tmp) < 4:
            tmp += str(num%2)
            num //= 2
        ans += tmp[::-1]
    res = ''
    print(ans, div)
    for i in range(0,len(ans),div):
        res += ans[i]
    return res

def check(li):
    deciphered_number = []
    check = even = odd = 0
    for idx, number in enumerate(li,start = 1):
        if idx % 2:
            odd += number
        else:
            even += number

        deciphered_number.append(number)
    even -= deciphered_number[-1]
    check = deciphered_number[-1]
    if (odd*3+even+check)%10 == 0:
        return True
    else:
        return False
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    encrypted_number = set([])
    for i in range(n):
        tmp = input()
        if tmp == '0'*len(tmp):
            continue
        else:
            tmp = tmp.split('0')
            while '' in tmp:
                tmp.remove('')
            for tt in tmp:
                encrypted_number.add(tt)
    encrypted_number = list(encrypted_number)
    print(encrypted_number)

    ans = 0
    for numb in encrypted_number:
        print(numb)
        tmp = hexa_to_binary(numb)
        idx = len(tmp)-1
        while tmp[idx] == '0':
            idx -= 1
        idx += 1
        deciphered_number = []
        start_idx = idx%7
        for i in range(start_idx, idx,7):
            deciphered_number.append(dic[tmp[i:i+7]])
        if check(deciphered_number):
            ans += sum(deciphered_number)
    print('#%d %d' % (t, ans))

#print('#%d %d' % (t, 0))

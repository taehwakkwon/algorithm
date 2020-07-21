def convert(number,base):
    res = ''
    number = int(number)
    while(number):
        res = num[number%base] + res
        number //= base
    return res


num = list('0123456789')
for i in range(65,65+55):
    num.append(chr(i))
T = int(input())
numbers = [input() for _ in range(T)]
ans = []
for i in range(T):
    n = len(numbers[i])
    for j in range(2,65):
        tmp = convert(numbers[i],j)
        if tmp == tmp[::-1]:
            ans.append(1)
            break
    else:
        ans.append(0)
for i in ans:
    print(i)
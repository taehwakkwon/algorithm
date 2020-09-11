import sys
sys.stdin = open('input.txt')


n = int(input())
ips = []
for t in range(n):
    tmp = list(map(int, input().split('.')))
    p = ''
    for i in range(4):
        ip = ''
        for j in range(8):
            if 1 << j & tmp[i]:
                ip += '1'
            else:
                ip += '0'
        p += ip[::-1]
    ips.append(p)

mask = ''
cnt = 0
flag = False
address = ''
for i in range(len(ips[0])):
    cnt += 1
    for j in range(1,len(ips)):
        if flag or ips[0][i] != ips[j][i]:
            mask += str(0)
            address += str(0)
            flag = True
            break
    else:
        mask += str(1)
        address += ips[0][i]
    if cnt == 8:
        cnt = 0
net_mask = ''
net_address = ''
for i in range(0,32,8):
    net_mask += str(int(mask[i:i+8], base=2)) + '.'
    net_address += str(int(address[i:i + 8], base=2)) + '.'

net_mask = net_mask[:-1]
net_address = net_address[:-1]
print(net_address)
print(net_mask)
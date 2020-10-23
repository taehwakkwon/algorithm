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
def get_encrypted_number():
    encrypted_numbers = []
    for i in range(n):
        if 1 not in board[i]:
            continue
        else:
            for j in range(m-1,-1,-1):
                if board[i][j] == 1:
                    break
            for p in range(j-55,j+1, 7):
                encrypted_numbers.append(''.join(map(str,board[i][p:p+7])))
            return encrypted_numbers

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input())) for _ in range(n)]
    encrypted_numbers = get_encrypted_number()


    deciphered_number = []
    check = even = odd = 0
    for idx, number in enumerate(encrypted_numbers,start = 1):
        num = dic[number]
        if idx % 2:
            odd += num
        else:
            even += num

        deciphered_number.append(num)
    even -= deciphered_number[-1]
    check = deciphered_number[-1]
    if (odd*3+even+check)%10 == 0:
        print('#%d %d' %(t, sum(deciphered_number)))
    else:
        print('#%d %d' % (t, 0))

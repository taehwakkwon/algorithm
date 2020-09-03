import sys
sys.stdin = open('input.txt','r')

def find_prime(number):
    if number == 1:
        return False
    for i in range(2,number):
        if number % i == 0 :
            return False
    else:
        return True
case_num = int(input())
result = []
num_list = list(map(int,input().split(' ')))
for jdx in num_list:
    result.append(find_prime(jdx))
else:
    print(result.count(True))
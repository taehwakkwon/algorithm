import sys
<<<<<<< HEAD
=======
sys.stdin = open("input.txt",'r')
import sys
>>>>>>> 33da9fd9c7f6f90040c922ff00c3fbb487d2d25d
input = sys.stdin.readline
def set(order, number = 0):
    global number_list
    if order == 'add' and number not in number_list:
        number_list.append(number)
    elif order == 'remove' and number in number_list:
        number_list.remove(number)
    elif order == 'check':
        if number in number_list:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if number in number_list:
            number_list.remove(number)
        else:
            number_list.append(number)
    elif order == 'all':
        number_list = [i for i in range(1,21)]
    elif order == 'empty':
        number_list = []


if __name__ == "__main__":
    M = int(input())
    number_list = []
    for i in range(M):
        inputs = input()
        if 'all' in inputs or 'empty' in inputs:
            set(inputs.rstrip(), 0)
        else:
            order, number = inputs.split()
<<<<<<< HEAD
            set(order.rstrip(), int(number))
=======
            set(order.rstrip(), int(number))
>>>>>>> 33da9fd9c7f6f90040c922ff00c3fbb487d2d25d

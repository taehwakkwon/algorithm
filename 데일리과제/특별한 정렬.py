import sys
sys.stdin = open('sample_input.txt')
def strange_sort(numbers):
    new_list = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    left = 0
    right = len(numbers) - 1
    while left < right:
        new_list.append(numbers[left])
        new_list.append(numbers[right])
        left += 1
        right -= 1

    return ' '.join(map(str,new_list[:10]))


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        n = int(input())
        numbers = list(map(int, input().split()))
        print('#%d %s' %(t, strange_sort(numbers)))


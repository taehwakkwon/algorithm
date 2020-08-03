def BubbleSort(number_list):
    for i in range(len(number_list) - 1, 0, -1):
        for j in range(0, i):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
data = [55, 7, 78, 12 ,42]
BubbleSort(data)
print(data)
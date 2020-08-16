import sys

sys.stdin = open('input.txt', 'r')
def transpose(arrays):
    transposed_arrays = []
    for i in range(len(arrays[0])):
        tmp = []
        for j in range(len(arrays)):
            tmp.append(arrays[j][i])
        transposed_arrays.append(tmp)
    return transposed_arrays

def sort(array):
    dict = []
    nums = set(array)
    for num in nums:
        if num == 0:
            continue
        dict.append((num, array.count(num)))
    dict_sorted = sorted(dict, key=lambda x: (x[1],x[0]))
    new_list = []
    for i in range(len(dict_sorted)):
        for j in range(len(dict_sorted[i])):
            new_list.append(dict_sorted[i][j])
    return new_list



if __name__ == "__main__":
    r,c,k = map(int, input().split())
    arrays = [list(map(int,list(input().split()))) for _ in range(3)]
    for i in range(101):
        try:
            if arrays[r - 1][c - 1] == k:
                print(i)
                break
            if arrays[r - 1][c - 1] >= 100:
                print(-1)
                break
        except IndexError:
            pass
        if len(arrays) >= len(arrays[0]):
            M = len(arrays)
            for i in range(len(arrays)):
                m = len(arrays[i])
                arrays[i] = sort(arrays[i])
                if M < len(arrays[i]):
                    M = len(arrays[i])
                if M < m:
                    M = m

            for i in range(len(arrays)):
                if len(arrays[i]) == M:
                    continue
                else:
                    for j in range(M-len(arrays[i])):
                        arrays[i].append(0)
        else:
            arrays = transpose(arrays)
            M = 0
            for i in range(len(arrays)):
                m = len(arrays[i])
                arrays[i] = sort(arrays[i])
                if M < len(arrays[i]):
                    M = len(arrays[i])
                if M < m:
                    M = m

            for i in range(len(arrays)):
                if len(arrays[i]) == M:
                    continue
                else:
                    for j in range(M-len(arrays[i])):
                        arrays[i].append(0)
            arrays = transpose(arrays)
        if len(arrays) > 100:
            print(-1)
            break
    else:
        print(-1)
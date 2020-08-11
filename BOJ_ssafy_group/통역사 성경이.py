import sys
sys.stdin = open('input.txt','r')

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    inputs = input()
    end = ['.','!','?']
    bf = 0
    sentence = []
    for i in range(len(inputs)):
        if inputs[i] in end:
            sentence.append(' ' + inputs[bf:i])
            bf = i + 2

    print('#%d' %t, end = ' ')
    for i in range(len(sentence)):
        flag = False
        j = 0
        cnt = 0
        while j < len(sentence[i]):
            if sentence[i][j] == ' ':
                flag = True
                j += 1
                if sentence[i][j].isalpha() and sentence[i][j].isupper():
                    k = j
                    k += 1
                    while len(sentence[i]) > k and sentence[i][k] != ' ':
                        if len(sentence[i]) > k and sentence[i][k].isalpha() and sentence[i][k].islower():
                            k += 1
                            continue
                        break
                    else:
                        cnt += 1
                    while len(sentence[i]) > k and sentence[i][k] != ' ':
                        k += 1
                    j = k
                else:
                    j += 1
            else:j += 1
        print(cnt, end = ' ')
    print()
def solution(n, delivery):
    dic = {i: 0 for i in range(1, n + 1)}
    check = ['?'] * (n + 1)
    for a, b, ch in delivery:
        if ch == 1:
            check[a] = check[b] = 'O'
            dic[a] += 1
            dic[b] += 1

    for a, b, ch in delivery:
        if ch == 0:
            if dic[a] > 0:
                dic[b] -= 1
                check[b] = 'X'
            if dic[b] > 0:
                dic[a] -= 1
                check[a] = 'X'
    return ''.join(check[1:])
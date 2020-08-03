def build_data(data):
    M = max(data)
    board = []
    for i in range(len(data)):
        tmp = []
        for j in range(M):
            if data[i]:
                tmp.append(1)
                data[i] -= 1
            else:
                tmp.append(0)
        board.append(tmp)
    m = 0
    for i in range(len(board)):
        for j in range(len(board[i])-1, -1,-1):
            if board[i][j]:
                cnt = 0
                for k in range(i + 1, len(board)):
                    if board[k][j] == 0:
                        cnt += 1
                    else:
                        continue
                    if m < cnt:
                        m = cnt
    return m

def build_data(data):
    M = 0
    for i in range(len(data)):
        cnt = 0
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                cnt += 1
        if M < cnt:
            M = cnt
    return M

if __name__ == "__main__":
    buldings = [7, 4, 2, 0, 0, 6, 0, 8, 7]
    print(build_data(buldings))
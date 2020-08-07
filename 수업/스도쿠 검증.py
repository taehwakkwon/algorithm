import sys
sys.stdin = open('input.txt')

def check_sudoku():
    for i in range(9):
        ch_r = [0] * 10
        ch_c = [0] * 10
        for j in range(9):
            ch_r[board[i][j]] += 1
            ch_c[board[j][i]] += 1
        if all([bool(ch_r[1] == ch_r[i]) for i in range(1,10)]) and all([bool(ch_c[1] == ch_c[i]) for i in range(1,10)]):
            pass
        else:
            print('#%d %d' %(t, 0))
            return
    for i in range(0,9,3):
        for j in range(0,9,3):
            ch_box = [0]*10
            for k in range(3):
                for l in range(3):
                    ch_box[board[i+k][j+l]] += 1
            if all([bool(ch_box[1] == ch_box[i]) for i in range(1,10)]):
                pass
            else:
                print('#%d %d' % (t, 0))
                return
    print('#%d %d' %(t, 1))
    return


if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        board = [list(map(int, input().split())) for _ in range(9)]
        check_sudoku()

    #r,c 검사

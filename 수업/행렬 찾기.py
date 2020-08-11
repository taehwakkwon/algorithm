import sys
sys.stdin = open('input.txt')

def find_sub_matrix():
    i, j = 0, 0
    infos = []
    for i in range(n):
        for j in range(n):
            if board[i][j] and ch[i][j] == 0:
                width = 0
                height = 0
                while j + width < n and board[i][j + width]:
                    width += 1
                while i + height < n and board[i+height][j]:
                    height += 1
                infos.append((height*width, height, width))
                for k in range(i, i + height):
                    for l in range(j, j + width):
                        ch[k][l] = 1
    return sorted(infos)

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        ch = [[0]*n for _ in range(n)]
        res = find_sub_matrix()
        print(res)
        print('#%d %d' %(t, len(res)), end = ' ')
        for r in res:
            print('%d %d' %(r[1],r[2]), end = ' ')
        print()



    #r,c 검사

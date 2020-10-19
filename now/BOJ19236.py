import sys
sys.stdin = open('input.txt')


'''
물고기
배열 값 1<= <=16
물고기 한칸 1마리
작은 물고기부터 이동
이동하려는 칸에 상어가 있을 떄 45도씩 회전(반시계)
자리 바꾸는 방식으로 이동
'''

'''
상어 0,0에 들어감
한번에 여러칸
이동과 동시에 물고기 먹고 같은 방향으로 회전(중간에 지나치는 먹이는 먹지 않음)
이동할 수 없으면 stop
'''

#상어가 먹고 물고기 이동
move = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
# def dfs(r,c,s):
#     if board[r][c]
#     pass

    #1-16까지만인자, 1-16 계속도는건지 모름
def shark_move(sr,sc,direc,had,v):
    global max_had
    def fish_move(v):
        if v not in fishes:
            fishes(v+1)
        fr, fc, direc = fishes[v]
        for i in range(8):
            nfr, nfc = fr + move[(direc+i)%8][0], fc + move[(direc+i)%8][1]
            if 0 <= nfr < 4 and 0 <= nfc < 4 and (nfr, nfc) != (sr, sc):
                print(board[fr][fc])
                print(fr,fc)
                board[fr][fc][1] = i
                board[nfr][nfc], board[fr][fc] = board[fr][fc], board[nfr][nfc]
                break

    if v == 17:
        max_had = max(max_had, had)
    if board[sr][sc]:
        had += board[sr][sc][0]

        direc = board[sr][sc][1]
        del fishes[board[sr][sc][0]]
        board[sr][sc] = []
        nsr, nsc = sr, sc
    else:
        nsr, nsc = sr , sc
        #역기서 재귀 타야함.. 다 갈 수 있으니까
        while 0 <= nsr + move[direc][0] < 4 and 0 <= nsc  + move[direc][1] < 4 and board[nsr][nsc] != []:
            nsr += move[direc][0]
            nsc += move[direc][1]

    fish_move(v+1)
    shark_move(nsr,nsc,direc,had,v+1)

def dfs(r,c, direc,had):
    if 0 <= r + move[direc][0] < 4 and 0 <= c + move[direc][1] < 4 and board[r+move[direc][0]][c+move[direc][1]]:
        #지우고
        dfs(r + move[direc][0], c + move[direc][1],board[r + move[direc][0]][c + move[direc][1]][1], had + board[r + move[direc][0]][c + move[direc][1]][0])
        #다시 넣어주기
    if 0 <= r + 2*move[direc][0] < 4 and 0 <= c + 2*move[direc][1] < 4 and board[r + 2*move[direc][0]][c + 2*move[direc][1]]:
        dfs(r + 2*move[direc][0], c + 2*move[direc][1],board[r + 2*move[direc][0]][c + 2*move[direc][1]][1], had + board[r + 2*move[direc][0]][c + 2*move[direc][1]][0])
    if 0 <= r + 3*move[direc][0] < 4 and 0 <= c + 3*move[direc][1] < 4 and board[r + 2*move[direc][0]][c + 2*move[direc][1]]:
        dfs(r + 3*move[direc][0], c + 3*move[direc][1],board[r + 3*move[direc][0]][c + 3*move[direc][1]][1], had + board[r + 3*move[direc][0]][c + 3*move[direc][1]][0])
    if 0 <= r + 4*move[direc][0] < 4 and 0 <= c + 4*move[direc][1] < 4 and board[r + 4*move[direc][0]][c + 4*move[direc][1]]:
        dfs(r + 4*move[direc][0], c + 4*move[direc][1],board[r + 4*move[direc][0]][c + 4*move[direc][1]][1], had + board[r + 4*move[direc][0]][c + 4*move[direc][1]][0])






board = [[0]*4 for _ in range(4)]
fishes = {}
idx = 0
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    board[i][0],board[i][1],board[i][2],board[i][3] = [a1,b1-1], [a2,b2-1], [a3,b3-1],[a4,b4-1] #물고기 번호, 방향
    fishes[a1],fishes[a2],fishes[a3],fishes[a4] = [i,0,b1-1],[i,1,b2-1],[i,2,b3-1],[i,3,b4-1]
print(fishes)
max_had = 0
for sr in range(4):
    for sc in range(4):
        first = board[sr][sc]
        board[sr][sc] = []
        dfs(sr,sc,first[0],first[1],1)
print(max_had)
import sys
sys.stdin = open('input.txt','r')


#아기상어 초기값:2
#작은 물고기만 먹을 수 있고, 큰 물고기 지나갈 수 없다.
#크기가 같은 물고기 먹을 수 없지만, 지나갈 수 있다.

#물고기 없으면 -> 엄마상어
#물고기 1마리면 -> 잡으러감
#가장 가까운 물고기(최단거리, 위)

#경험치:자기 크기



if __name__ == "__main__":
    n = int(input())
    baby_shark = 2
    had_fish = []
    space = [list(map(int,input().split())) for _ in range(n)]



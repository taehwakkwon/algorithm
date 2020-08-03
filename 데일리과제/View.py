import sys
sys.stdin = open('sample_input.txt')

def build_data(buildings):
    cnt = 0
    for i in range(2, len(buildings) - 2):
        for j in range(buildings[i], 0, -1):
            tmp = []
            for k in range(1, 3):
                if buildings[i + k] < j and buildings[i - k] < j:
                    tmp.append(True)
            if tmp == [True, True]:
                cnt += 1
            else:
                break
    return cnt

if __name__ == "__main__":
    t = 10
    for i in range(t):
        n = int(input())
        buildings = list(map(int ,input().split()))
        print('#%d %d ' %(i + 1, build_data(buildings)))
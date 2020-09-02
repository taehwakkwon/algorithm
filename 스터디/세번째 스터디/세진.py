import sys
sys.stdin = open('input.txt')
def combinations(v, s, res):
    if v == 2:
        r.append(tuple(res[:]))
        return
    else:
        for i in range(s, n):
            combinations(v + 1, i + 1, res + [i])

def search(visited):
    global result
    # 입력받은 score와 비교해서 더 큰게 있으면 return
    for i in range(18):
        if check[i] > score[i]:
            return
    # 원하는 결과가 있는 경우 result를 1로 바꾸고 return
    if check == score and len(visited) == 15:
        result = 1

    # i j 가 이기고 비기고 지는 모든 경우에 대해서 검증. 6Combination2 = 15가지 경우
    # list[3*i], list[3*i+1], list[3*i+2] 각각 i팀 승 무 패
    for i, j in r:
        # i win j lose
        if (i,j) in visited:
            continue
        visited.append((i,j))
        check[ 3 *i] += 1
        check[ 3 * j +2] += 1
        search(visited)
        check[ 3 *i] -= 1
        check[ 3 * j +2] -= 1
        # i draw j draw
        check[ 3 * i +1] += 1
        check[ 3 * j +1] += 1
        search(visited)
        check[ 3 * i +1] -= 1
        check[ 3 * j +1] -= 1
        # i lose j win
        check[ 3 * i +2] += 1
        check[ 3 *j] += 1
        search(visited)
        check[ 3 * i +2] -= 1
        check[ 3 *j] -= 1

n = 6
r = []
combinations(0, 0, [])
answer = []
for tc in range(4):
    score = list(map(int ,input().split()))
    check = [0] * 18
    result = 0

    search([])
    answer.append(result)

for i in answer:
    print(i, end=' ')
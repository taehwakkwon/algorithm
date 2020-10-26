def dfs(step, count, score):
    global max_score
    # print(step,count,score)
    if count > m + 1:
        return
    if step > n:#도착범위 들어올 때
        if count == m + 1: #도착지점도 카운트했기 때문에 + 1
            max_score = max(max_score, score)
    else:
        dfs(step + 1, count + 1, score + stones[step + 1]) #1스텝 가는경우
        dfs(step + 2, count + 1, score + stones[step + 2]) #2스텝 가는경우


T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    stones = [0] + list(map(int, input().split())) + [0,0] #출발, 도착점 생성
    max_score = 0
    dfs(0,0,0)
    print('#%d %d' %(t,max_score))




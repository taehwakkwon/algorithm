def solution(arr):
    def check(r, c, size):
        num = arr[r][c]
        for i in range(size):
            for j in range(size):
                if arr[r+i][c+j] == num and visited[r+i][c+j] == 0:
                    continue
                else:
                    return False
        return True

    def cal(r, c, size):
        num = arr[r][c]
        if num == 1:
            for i in range(size):
                for j in range(size):
                    arr[r+i][c+j] = 0
                    visited[r+i][c+j] = size
            count[1] += 1
        else:
            for i in range(size):
                for j in range(size):
                    arr[r+i][c+j] = 0
                    visited[r+i][c+j] = size
            count[0] += 1



    N = len(arr)
    n = -1
    psum = [[0]*(N+1) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    count = [0,0]

    for i in range(N):
        for j in range(N):
            psum[i][j+1] = psum[i][j] + arr[i][j]
    while N:
        N //= 2
        n += 1
    N = 2 ** n
    for i in range(n, -1, -1):
        size = 2 ** i
        for p in range(0, N, size):
            for q in range(0, N, size):
                if check(p, q, size):
                    cal(p, q, size)
    return count


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
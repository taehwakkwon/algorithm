def solution(board):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    m = 0
    #네방향, 회전
    def dfs(r1, c1, r2, c2, d, s):
        global m
        if (r1, c1) == (n - 1, n - 1) or (r2, c2) == (n - 1, n - 2):
            if s < m:
                s = m
            return
        else:
            for dr, dc in move:
                new_r1, new_c1, new_r2, new_c2 = r1 + dr, c1 + dc, r2 + dr, c2 + dc
                if 0 <= new_r1 < n and 0 <= new_c1 < n and 0 <= new_c2 < n and 0 <= new_r2 < n and not visited[r1][c1] == visited[r2][c2] == 1:




                new_r1, new_c1, new_r2, new_c2 = r1 + dr[d], c1 + dc[d], r2 + dr[d], c2 + dc[d]
                if 0 <= new_r1 < n and 0 <= new_c1 < n and 0 <= new_r2 < n and 0 <= new_c2 < n and board[new_r1][new_c1] == board[new_r2][new_c2] == 0 and visited[new_r1][new_c1] != d and visited[new_r2][new_c2] != d:
                    visited[new_r1][new_c1] = visited[new_r2][new_c2] = d
                    dfs(r1 + dr[d], c1 + dc[d], r2 + dr[d], c2 + dc[d], d, s + 1)
                    visited[new_r1][new_c1] = visited[new_c2][new_c2] = 0
    answer = 0
    return answer
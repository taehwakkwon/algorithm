
def hourglassSum(arr):
    check = [(0 ,0) ,(0 ,1) ,(0 ,2) ,(1 ,1) ,(2 ,0) ,(2 ,1) ,(2 ,2)]
    M = -float('inf')
    for r in range(len(arr ) -2):
        for c in range(len(arr ) -2):
            cnt = 0
            for dr, dc in check:
                nr, nc = r + dr, c + dc
                cnt += arr[nr][nc]
            M = max(M, cnt)
    return M

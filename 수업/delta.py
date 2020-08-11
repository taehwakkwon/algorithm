
arr = [[1,2,3],[4,5,6],[7,8,9]]
r, c = 1, 1
sum_v = 0
for dr, dc in [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]:
    nr = r + dr
    nc = c + dc
    sum_v += arr[nr][nc]
print(sum_v)
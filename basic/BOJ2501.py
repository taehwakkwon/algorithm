p, q = map(int, input().split())
res = []
for idx in range(1,p+1):
    if not p % idx:
        res.append(idx)
else:
    if len(res) > q-1:
        print(res[q-1])
    else:
        print(0)
def dfs(n):
    if n >= 3:
        for i in range(3):
            if ch[i] == 1:
                print(i+1, end = ' ')
        print()
    else:
        ch[n] = 1
        dfs(n+1)
        ch[n] = 0
        dfs(n+1)

if __name__ == "__main__":
    ch = [0]*3
    dfs(0)
def fib(n):
    if n == 0:
        return [1, 0]
    if n == 1:
        return [0, 1]
    if len(numbers) > n:
        return numbers[n]
    numbers.append([fib(n-1)[0] + fib(n-2)[0], fib(n-1)[1] + fib(n-2)[1]])
    return numbers[n]

if __name__ == "__main__":
    t = int(input())
    numbers = [[1,0],[0,1]]
    result = []
    for i in range(t):
        result.append(fib(int(input())))
    for r in result:
        print(r[0],r[1])
    
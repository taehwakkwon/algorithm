def gcd(a,b):
    L = a*b
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    t = int(input())
    result = []
    for _ in range(t):
        total = 0
        numbers = list(map(int, input().split()))
        for i in range(1,len(numbers)):
            for j in range(i+1,len(numbers)):
                total += gcd(numbers[i],numbers[j])
        result.append(total)
    for r in result:
        print(r)
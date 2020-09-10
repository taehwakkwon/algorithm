def solution(numbers):
    n = len(numbers)
    result = []
    for i in range(n):
        for j in range(i+1, n):
            result.append(numbers[i] + numbers[j])
    return sorted(list(set(result)))
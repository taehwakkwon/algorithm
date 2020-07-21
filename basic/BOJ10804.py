def change_sequence(a, b, nums):
    res = []
    res.extend(nums[:a])
    res.extend(nums[a:b + 1][::-1])
    res.extend(nums[b + 1:])
    return res


nums = list(range(1, 21))
for _ in range(10):
    a, b = map(int, input().split())
    nums = change_sequence(a - 1, b - 1, nums)
for num in nums:
    print(num, end=' ')

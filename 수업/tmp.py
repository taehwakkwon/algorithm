def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def max(*args):
    M = args[0]
    for number in args[1:]:
        if M < number:
            M = number
    return M
print(max(1, 2, 3))
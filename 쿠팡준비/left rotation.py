from collections import deque
def rotLeft(a, d):
    a = deque(a)
    a.rotate(-d)
    return list(a)
'''
1 2 3 4 5
한사람이 두사람에게만 뇌물 줄 수 있음
t에서 두사람 뒤로 보냈을 때 원위치가 된다면?
'''

def minimumBribes(q):
    bribes = 0
    mins = [float('inf'), float('inf')]

    for i, p in reversed(list(enumerate(q, 1))):
        if p - i > 2:
            print('Too chaotic')
            return
        elif p > mins[1]:
            bribes += 2
        elif p > mins[0]:
            bribes += 1

        if p < mins[0]:
            mins = (p, mins[0])
        elif p < mins[1]:
            mins = (mins[0],p)
    print(bribes)

def solution(play_time, adv_time, logs):
    def add(time1, time2):
        h1, m1, s1 = map(int, time1.split(':'))
        h2, m2, s2 = map(int, time2.split(':'))
        new_h, new_m, new_s = h1 + h2, m1 + m2, s1 + s2
        if new_s >= 60:
            new_s -= 60
            new_m += 1
        if new_m >= 60:
            new_m -= 60
            new_h += 1
        new_h, new_m, new_s = map(str, [new_h, new_m, new_s])
        while len(new_s) < 2:
            new_s = '0' + new_s
        while len(new_m) < 2:
            new_m = '0' + new_m
        while len(new_h) < 2:
            new_h = '0' + new_h
        return new_h + ':' + new_m + ':' + new_s

    def minus(time1, time2):
        if time1 < time2:
            time1, time2 = time2, time1
        h1, m1, s1 = map(int, time1.split(':'))
        h2, m2, s2 = map(int, time2.split(':'))

        new_h, new_m, new_s = h1 - h2, m1 - m2, s1 - s2
        if new_s < 0:
            new_s += 60
            new_m -= 1
        if new_m < 0:
            new_m += 60
            new_h -= 1

        new_h, new_m, new_s = map(str, [new_h, new_m, new_s])
        while len(new_s) < 2:
            new_s = '0' + new_s
        while len(new_m) < 2:
            new_m = '0' + new_m
        while len(new_h) < 2:
            new_h = '0' + new_h
        return new_h + ':' + new_m + ':' + new_s

    new_log = []
    for i in range(len(logs)):
        s, e = logs[i].split('-')
        new_log.append('s' + s)
        new_log.append('e' + e)
    n = len(new_log)
    new_log = sorted(new_log, key=lambda x: x[1:])
    cnt = 0
    M, value = '00:00:00', '00:00:00'

    for i in range(1,len(new_log)):
        if new_log[i][0] == 's':
            start = new_log[i][1:]
            end_adv = add(start + adv_time)
            tmp = []
            if end_adv > play_time:
                continue
            else:
                for j in range(i + 1, len(new_log)):




    if value == '00:00:00':
        return '00:00:00'
    else:
        return minus(value, adv_time)
print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
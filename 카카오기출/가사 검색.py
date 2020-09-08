def solution(words, queries):
    def check(key):
        cnt = 0
        n = len(key)
        for word in words:
            if len(word) != n:
                continue
            for i in range(n):
                if key[i] == '?':
                    continue
                if word[i] != key[i]:
                    break
            else:
                cnt += 1
        return cnt
    ans = []
    for query in queries:
        ans.append(check(query))
    return ans


def solution(words, queries):
    def check(key):
        cnt = 0
        n = len(key)
        if key[0] == '?':
            for i in range(1, len(key)):
                if key[i] != '?':
                    core = key[i:]
                    break
        else:
            i = key.index('?')
            core = key[:i]

        for word in words:
            if len(word) == n and (core == word[i:] or core == word[:i]):
                cnt += 1
        return cnt

    ans = []
    for query in queries:
        ans.append(check(query))
    return ans


def solution(words, queries):
    def check(key):
        cnt = 0
        n = len(key)
        if key[0] == '?':
            if len(key) < 2:
                core = ''
                i = 0
            else:
                for i in range(1, len(key)):
                    if key[i] != '?':
                        core = key[i:]
                        break
        else:
            i = key.index('?')
            core = key[:i]

        for word in words:
            if len(word) == n and (core == word[i:] or core == word[:i]):
                cnt += 1
        return cnt

    ans = []
    for query in queries:
        ans.append(check(query))
    return ans

print(solution(['a','bb'], ['?']))

word, queries = ["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]
solution(word, queries)


def solution(words, queries):
    def check(key):
        cnt = 0
        n = len(key)
        if key[0] == '?':
            for i in range(1, len(key)):
                if key[i] != '?':
                    core = key[i:]
                    break
        else:
            i = key.index('?')
            core = key[:i]

        for word in words:
            if len(word) == n and (core == word[i:] or core == word[:i]):
                cnt += 1
        return cnt

    ans = []
    for query in queries:
        ans.append(check(query))
    return ans
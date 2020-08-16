import sys

name = sorted(list(input()))
dic = {}
for string in name:
    dic[string] = dic.get(string,0) + 1
if len(name) % 2 == 0 and any([bool(x%2) for x in dic.values()]):
    print("I'm Sorry Hansoo")
else:
    pal = ''
    last = ''
    for key in dic:
        while dic[key]:
            if dic[key] == 1:
                last += key
                dic[key] -= 1
                if len(last) > 1:
                    print("I'm Sorry Hansoo")
                    sys.exit()
                continue
            pal += key
            dic[key] -= 2
    print(pal + last + pal[::-1])

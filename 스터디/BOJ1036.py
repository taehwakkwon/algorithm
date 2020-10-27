import sys
sys.stdin = open('input.txt')
numbers = list(map(str,range(10))) + list(map(chr, range(65,91)))
n = int(input())
cnt = 0
words = [input().rstrip() for _ in range(n)]
k = int(input())
dic = {}
for word in words:
    for idx,letter in enumerate(word[::-1]):
        dic[letter] = dic.get(letter,0) + (35-numbers.index(letter))*36**idx

dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

changed = []
for key, value in dic[:k]:
    changed.append(key)

for word in words:
    for idx, letter in enumerate(word[::-1]):
        if letter in changed:
            letter = 'Z'
        cnt += numbers.index(letter)*(36**idx)

ans = ''
while cnt:
    ans += numbers[cnt % 36]
    cnt //= 36
if ans:
    print(ans[::-1])
else:
    print(0)

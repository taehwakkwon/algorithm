#대문자 -> 소문자
#소문자, 숫자, - _ . 빼고 다 제외
#.. -> .
#마침표 처음이나 끝에 있으면 제거
#비었으면 a 대입
#16자 이상이면, 15까지만 그리고 맨 뒤가 .이면 .도 제거
#2자 이하면, -1문자를 붙임 길이가 3까지
def solution(new_id):
    alpha = list(map(chr, range(ord('a'),ord('z')+1))) + list(map(str,range(10))) + ['-','_','.']
    new_id = new_id.lower()
    id = ''
    for i in range(len(new_id)):
        if new_id[i] in alpha:
            id += new_id[i]

    while '..' in id:
        id = id.replace('..', '.')

    if id and id[0] == '.':
        id = id[1:]
    if id == '':
        id = 'a'

    id = id[:15]
    if id[-1] == '.':
        id = id[:-1]

    while len(id) <= 2:
        id += id[-1]

    return id

# print(solution(''))
# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
#정규식

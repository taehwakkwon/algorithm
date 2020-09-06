def solution(files):
    alpha = list(map(chr, range(ord('A'), ord('Z') + 1))) + [' ', '.', '-']
    new_files = []
    for i in range(len(files)):
        head, number = '', ''
        j = 0
        while j < len(files[i][j]) and not files[i][j].isdigit():
            head += str(alpha.index(files[i][j].upper()))
            j += 1

        while j < len(files[i][j]) and files[i][j].isdigit():
            number += files[i][j]
            j += 1

        new_files.append([head] + [int(number)] + [i])
    new_files = sorted(new_files, key=lambda x: [x[0], x[1], x[2]])
    answer = []

    for i in new_files:
        answer.append(files[i[-1]])
    return answer


a = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
b = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

solution(a)










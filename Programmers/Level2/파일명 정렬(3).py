import re

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
    answer = []

    for file in files:
        head, number, tail = '', '', ''

        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                break

        for i in range(len(number)):
            if not number[i].isdigit():
                tail = number[i:]
                number = number[:i]
                break
        
        answer.append([head, number, tail])

    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))

    return [''.join(i) for i in answer]

print(solution(files))
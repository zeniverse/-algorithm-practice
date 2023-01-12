
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
    res = []
    idx = 0

    for file in files:
        head = ''
        number = ''
        flag = False
        for i in range(len(file)):
            if file[i].isdigit() and len(number) < 5:
                flag = True
                number += file[i]
            elif not flag:
                head += file[i].upper()
            elif flag:
                break
        res.append([head, int(number), idx, file])
        idx += 1

    res.sort()
    return [res[i][3] for i in range(len(files))]

print(solution(files))
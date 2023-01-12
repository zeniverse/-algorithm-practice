import re

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    res = sorted(temp, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(f) for f in res]

print(solution(files))
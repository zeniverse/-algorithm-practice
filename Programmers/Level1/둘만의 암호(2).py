from string import ascii_lowercase

def solution(s, skip, index):
    res = ''
    aToz = set(ascii_lowercase)
    aToz -= set(skip)
    aToz = sorted(aToz)
    l = len(aToz)

    dic = {alpha : idx for idx, alpha in enumerate(aToz)}
    print(dic)

    for i in s:
        res += aToz[(dic[i] + index) % l]
    
    return res

s = "aukks"
skip = "wbqd"
index = 5

print(solution(s, skip, index))


def solution(s, skip, index):
    res = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in skip:
        if i in alpha:
            alpha = alpha.replace(i, "")

    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        res += change
    
    return res

s = "aukks"
skip = "wbqd"
index = 5

print(solution(s, skip, index))

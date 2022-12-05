
my_string = "1a2b3c4d123Z"

def solution(my_string):
    res = 0
    tmp = ''

    for i in my_string:
        if i.isalpha():
            if len(tmp) != 0:
                res += int(tmp)
                tmp = ''
        else:
            tmp += i

    if len(tmp) != 0:
        res += int(tmp)

    return res

print(solution(my_string))

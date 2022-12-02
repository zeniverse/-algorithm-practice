my_string = "aAb1B2cC34oOp"

def solution(my_string):

    res = 0

    for i in my_string:
        if i.isdigit():
            res += int(i)

    return res

print(solution(my_string))

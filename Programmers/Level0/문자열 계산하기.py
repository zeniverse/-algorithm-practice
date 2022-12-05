
my_string = "3 + 4 - 7 + 1"

def solution(my_string):
    res = 0
    flag = True

    for i in my_string.split():
        if i.isdigit():
            if flag:
                res += int(i)
            else:
                res -= int(i)
        else:
            if i == '+':
                flag = True
            else:
                flag = False

    return res

print(solution(my_string))

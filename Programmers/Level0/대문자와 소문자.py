my_string = "cccCCC"

def solution(my_string):
    res = ''

    for i in my_string:
        if i.isupper():
            res += i.lower()
        else:
            res += i.upper()

    return res

print(solution(my_string))

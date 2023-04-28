
def solution(my_string):
    res = []
    for str in my_string.split(" "):
        if str != "":
            res.append(str)
    return res

my_string = "    programmers  "
print(solution(my_string))

def solution(my_string):
    return [i for i in my_string.split(" ") if i != ""]

my_string = "    programmers  "
print(solution(my_string))
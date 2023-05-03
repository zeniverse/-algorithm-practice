
def solution(my_string, m, c):
    res = ''
    for i in range(0, len(my_string), m):
        res += my_string[i + (c - 1)]
    return res

my_string = "ihrhbakrfpndopljhygc"
m, c = 4, 2
print(solution(my_string, m, c))
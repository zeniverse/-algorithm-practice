
def solution(my_string, m, c):
    return my_string[c - 1::m]

my_string = "ihrhbakrfpndopljhygc"
m, c = 4, 2
print(solution(my_string, m, c))
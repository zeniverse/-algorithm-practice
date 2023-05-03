
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e + 1][::-1] + my_string[e + 1:]

my_string = "Progra21Sremm3"
s, e = 6, 12
print(solution(my_string, s, e))
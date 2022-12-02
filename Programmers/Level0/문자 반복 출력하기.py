my_string = "hello"
n = 3

def solution(my_string, n):
    res = ''

    for i in my_string:
        res += i * n
    
    return res

print(solution(my_string, n))
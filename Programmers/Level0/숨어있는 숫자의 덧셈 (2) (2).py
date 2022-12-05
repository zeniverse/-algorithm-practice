
my_string = "1a2b3c4d123Z"

def solution(my_string):
    res = 0
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

print(solution(my_string))


my_string = "We are the world"

def solution(my_string):
    res = ''
    arr = []

    for i in my_string:
        if i not in arr:
            res += i
            arr.append(i)
                
    return res

print(solution(my_string))

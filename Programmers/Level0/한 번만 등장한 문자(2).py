
s = 'hello'

def solution(s):
    arr = list(s)
    arr.sort()
    
    res = ''

    for i in arr:
        if s.count(i) == 1:
            res += i

    return res


print(solution(s))

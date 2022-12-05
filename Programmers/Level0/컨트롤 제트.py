
s = "-1 -2 -3 Z"

def solution(s):
    arr = []

    for i in s.split():
        if i.isalpha():
            arr.pop(-1)
        else:
            arr.append(int(i))

    return sum(arr)


print(solution(s))

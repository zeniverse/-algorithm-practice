
s = "-1 -2 -3 Z"

def solution(s):
    stack = []

    for i in s.split():
        if i == 'Z':
            stack.pop()
        else:
            stack.append(int(i))

    return sum(stack)


print(solution(s))

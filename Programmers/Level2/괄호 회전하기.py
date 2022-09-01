

s = "[)(]"


def check(s):

    stack = []
    left = ['(', '[', '{']
    right = [')', ']', '}']

    for i in s:
        if i in left:
            stack.append(i)
        else:
            if stack:
                index = right.index(i)

                if stack[-1] == left[index]:
                    stack.pop()
                else:
                    return False
            else:
                return False

    if stack:
        return False
    else:
        return True
                


def solution(s):
    count = 0
    res = 0

    while count < len(s):
        if check(s):
            print(s)
            res += 1

        s = s[1:] + s[0]
        count += 1

    return res

print(solution(s))

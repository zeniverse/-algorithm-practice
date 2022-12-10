
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]

def solution(ingredient):
    res = 0
    stack = []

    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            res += 1
            for i in range(4):
                stack.pop()
    return res

print(solution(ingredient))
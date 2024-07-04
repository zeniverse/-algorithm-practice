
def solution(numbers):
    res = [-1] * len(numbers)
    stack = []

    for i , num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()
            res[idx] = num
        stack.append(i)

    return res

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
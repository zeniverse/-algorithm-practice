
order = [5, 4, 3, 2, 1]

def solution(order):
    answer = 0
    stack = []

    for idx, num in enumerate(order):
        stack.append(idx + 1)

        while stack and stack[-1] == order[answer]:
            stack.pop()
            aswer += 1
    
    return answer

print(solution(order))
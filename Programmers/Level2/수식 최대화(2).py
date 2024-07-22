from itertools import permutations
import re

def toPostfix(priority, arr):
    stack = [] # 연산자 스택
    postfix = []

    for i in arr:
        if i.isdigit():
            postfix.append(i)
        else:
            if not stack:
                stack.append(i)
            else:
                while stack:
                    if priority[i] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else:
                        break

                stack.append(i)

    while stack:
        postfix.append(stack.pop())

    return postfix

def calc(p):
    stack = []

    for i in p:
        if i.isdigit():
            stack.append(int(i))
            continue

        num1 = stack.pop()
        num2 = stack.pop()

        if i == '+':
            stack.append(num2 + num1)
        elif i == '-':
            stack.append(num2 - num1)
        else:
            stack.append(num2 * num1)

    return stack.pop()

def solution(expression):
    answer = 0
    
    arr = re.split("([-+*])", expression)

    for i in permutations(['-', '+', '*']):
        priority = {o:idx for idx, o in enumerate(list(i))}
        postfix = toPostfix(priority, arr)
        answer = max(answer, abs(calc(postfix)))             
    return answer


expression = "100-200*300-500+20"

print(solution(expression))



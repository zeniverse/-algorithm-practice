from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    
    for priority in list(permutations(['-', '+', '*'])):
        answer = max(answer, abs(make_result(priority, expression)))               
    return answer


def make_result(priority, expression):
    arr = deque()
    num = ''

    for i in expression:
        if i.isdigit():
            num += i
        else:
            arr.append(num)
            num = ''
            arr.append(i)

    arr.append(num)


    for op in priority:
        stack = []

        while arr:
            tmp = arr.popleft()
            if tmp == op:
                res = str(eval(stack.pop()+op+arr.popleft()))
                stack.append(res)
            else:
                stack.append(tmp)
        arr = deque(stack)
    return int(arr.pop())

expression = "100-200*300-500+20"

print(solution(expression))



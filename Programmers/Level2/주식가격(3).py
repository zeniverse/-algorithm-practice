
prices = [1, 2, 3, 2, 3]

def solution(prices):
    length = len(prices)
    answer = [i for i in range(length - 1, -1, -1)]

    stack = [0]

    for i in range(1, length):
        if stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = j - i
        stack.append(i)
    
    return answer

print(solution(prices))

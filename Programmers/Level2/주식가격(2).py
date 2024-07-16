from collections import deque

prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        period = 0
        price = queue.popleft()

        for after in queue:
            period += 1
            if price > after:
                break
        answer.append(period)

    return answer

print(solution(prices))

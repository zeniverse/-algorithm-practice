price = 3
money = 20
count = 4

def solution(price, money, count):
    return max(0, price * (count + 1) * count // 2 - money)

print(solution(price, money, count))









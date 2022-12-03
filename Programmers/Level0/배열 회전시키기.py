
numbers = [4, 455, 6, 4, -1, 45, 6]
direction = "left"

def solution(numbers, direction):
    res = []

    if direction == "right":
        res.append(numbers.pop(-1))
        res.extend(numbers)
    else:
        num = numbers.pop(0)
        res.extend(numbers)
        res.append(num)
        
    return res


print(solution(numbers, direction))


numbers = [4, 455, 6, 4, -1, 45, 6]
direction = "left"

def solution(numbers, direction):
    if direction == "right":
        return numbers[-1:] + numbers[:-1]
    else:
        return numbers[1:] + numbers[:1]
        


print(solution(numbers, direction))

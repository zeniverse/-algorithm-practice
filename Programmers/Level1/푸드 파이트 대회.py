
food = [1, 3, 4, 6]

def solution(food):
    left = []
    right = []

    for i in range(1, len(food)):
        for j in range(food[i]//2):
            left.append(i)
            right.append(i)
            
    left.append(0)
    left.extend(right[::-1])

    return "".join(map(str, left))

print(solution(food))
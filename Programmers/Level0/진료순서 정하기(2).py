
emergency = [3, 76, 24]

def solution(emergency):
    arr = sorted(emergency, reverse=True)
    return [arr.index(i) + 1 for i in emergency]


print(solution(emergency))

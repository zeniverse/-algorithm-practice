import copy

emergency = [3, 76, 24]

def solution(emergency):
    res = []

    arr = copy.deepcopy(emergency)
    arr.sort(reverse= True)

    for i in emergency:
        res.append(arr.index(i) + 1)

    return res
    


print(solution(emergency))

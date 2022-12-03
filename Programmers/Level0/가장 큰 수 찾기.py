array = [1, 8, 3]

def solution(array):
    res = []
    res.append(max(array))
    res.append(array.index(res[0]))

    return res


print(solution(array))

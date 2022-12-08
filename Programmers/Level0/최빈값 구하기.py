from collections import Counter

array = [1]

def solution(array):
    lst = Counter(array).most_common()
    maxValue = lst[0][1]
    res = lst[0][0]

    for i in range(1, len(lst)):
        if lst[i][1] == maxValue:
            return -1
        else:
            break
    
    return res
    
print(solution(array))
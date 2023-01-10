
elements = [7,9,1,1,4]

def solution(elements):
    res = set(elements)
    arr = elements + elements

    for i in range(2, len(elements) + 1):
        for j in range(len(elements)):
            res.add(sum(arr[j:j + i]))
    return len(res)

print(solution(elements))

def solution(citations):
    res = 0
    citations.sort(reverse = True)

    for i in citations:
        if i > res:
            res += 1

    return res

citations = [3, 0, 6, 1, 5]
print(solution(citations))


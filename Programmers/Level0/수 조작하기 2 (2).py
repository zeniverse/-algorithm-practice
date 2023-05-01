
def solution(numLog):
    res = ''
    match = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    for i in range(1, len(numLog)):
        res += match[numLog[i] - numLog[i - 1]]
    return res

numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(numLog))
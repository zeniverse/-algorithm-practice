
def solution(numLog):
    res = ''
    for i in range(1, len(numLog)):
        find = numLog[i] - numLog[i - 1]
        if find == 1:
            res += 'w'
        elif find == -1:
            res += 's'
        elif find == 10:
            res += 'd'
        else:
            res += 'a'
    return res

numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(numLog))
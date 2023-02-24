

def solution(gems):
    res = [0, len(gems) - 1]
    find = len(set(gems))
    length = len(gems)
    dic = {gems[0] : 1}

    left = 0
    right = 0

    while left < length and right < length:
        if len(dic) < find:
            right += 1

            if right == length:
                break

            dic[gems[right]] = dic.get(gems[right], 0) + 1
        else:
            if right - left + 1 < res[1] - res[0] + 1:
                res = [left, right]
            
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1

            left += 1
    
    return [res[0] + 1, res[1] + 1]

gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))

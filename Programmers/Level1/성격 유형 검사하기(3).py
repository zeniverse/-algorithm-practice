
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    dic = {"RT":0, "CF":0, "JM":0, "AN":0}

    for s, c in zip(survey, choices):
        if s not in dic.keys():
            s = s[::-1]
            dic[s] -= c - 4
        else:
            dic[s] += c - 4

    answer = ''

    for name in dic.keys():
        if dic[name] > 0:
            answer += name[1]
        else:
            answer += name[0]

    return answer

print(solution(survey, choices))
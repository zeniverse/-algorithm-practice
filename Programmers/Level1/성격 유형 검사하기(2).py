from collections import defaultdict

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    indicator = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'n')]
    answer = ''
    dic = defaultdict(int)

    for s, c in zip(survey, choices):
        if c < 4:
            dic[s[0]] += (4 - c)
        else:
            dic[s[1]] += (c - 4)
    
    for i in indicator:
        if dic[i[0]] >= dic[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    
    return answer

print(solution(survey, choices))

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]


def check(s):
    if res[s[0]] >= res[s[1]]:
        return s[0]
    return s[1]

def solution(survey, choices):
    global res
    
    answer = ''
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    res = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
        
    
    for i in range(len(survey)):
        if choices[i] < 4:
            res[survey[i][0]] += score[choices[i]]
        else:
            res[survey[i][1]] += score[choices[i]]
            
    answer += check("RT")
    answer += check("CF")
    answer += check("JM")
    answer += check("AN")
    return answer

print(solution(survey, choices))
def solution(n, m, section):
    answer = 1
    current = section[0] + m - 1
    
    for i in range(1, len(section)):
        if current < section[i]:
            answer += 1
            current =  section[i] + m - 1
            
    return answer

n, m = 16, 4
section = [2, 3, 15, 16]

print(solution(n, m, section))

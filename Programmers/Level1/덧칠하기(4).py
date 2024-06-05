def solution(n, m, section):
    answer = 1
    prev = section[0]

    for sec in section:
        if sec- prev >= m:
            answer += 1
            prev = sec
            
    return answer

n, m = 16, 4
section = [2, 3, 15, 16]

print(solution(n, m, section))

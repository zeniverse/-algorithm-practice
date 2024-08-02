
n = 4

def solution(n):
    answer = [0, 3, 11]
    idx = n // 2

    if n % 2:
        return 0
    
    if idx < 3:
        return answer[idx]
    
    for i in range(3, idx + 1):
        answer.append((answer[i - 1] * 3 + sum(answer[:i - 1]) * 2 + 2) % 1000000007)

    return answer[idx]

print(solution(n))
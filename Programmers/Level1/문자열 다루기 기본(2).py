
def solution(s):
    return s.isdigit() and len(s) in (4, 6)

print(solution("a234"))
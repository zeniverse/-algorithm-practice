
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isalpha():
                return False
    else:
        return False
    
    return True

print(solution("a234"))
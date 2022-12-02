
s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]

def solution(s1, s2):
    res = 0 

    for i in s1:
        if i in s2:
            res += 1

    return res

print(solution(s1, s2))
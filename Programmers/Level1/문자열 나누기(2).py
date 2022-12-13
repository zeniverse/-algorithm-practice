
s = "banana"

def solution(s):
    res = 0
    same = 0
    diff = 0

    for i in s:
        if same == diff:
            res += 1
            first = i

        if first == i:
            same += 1
        else:
            diff += 1
        
    return res
        

print(solution(s))
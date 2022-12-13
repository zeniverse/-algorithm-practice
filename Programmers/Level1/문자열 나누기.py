
s = "aaabbaccccabba"

def solution(s):
    res = 0

    idx = 0
    while idx < len(s):
        same = 1
        diff = 0
        first = s[idx]

        for i in range(idx + 1, len(s)):
            if first == s[i]:
                same += 1
            else:
                diff += 1

            if same == diff:
                res += 1
                idx = i + 1
                break

        if same != diff:
            res += 1
            break
        
    return res
        

print(solution(s))
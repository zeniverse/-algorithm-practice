
def solution(code):
    res = ""
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":
            mode ^= 1
        else:
            if i % 2 == mode:
                res += code[i]

    return res if res else "EMPTY"
        
code = "abc1abc1abc"
print(solution(code))
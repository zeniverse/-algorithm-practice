
def solution(code):
    res = ""
    mode = False
    for i in range(len(code)):
        if not mode and code[i] != "1" and i % 2 == 0:
            res += code[i]
        elif mode and code[i] != "1" and i % 2 != 0:
            res += code[i]
        elif code[i] == "1":
            mode = not mode

    return res if res else "EMPTY"
        

        
code = "abc1abc1abc"
print(solution(code))
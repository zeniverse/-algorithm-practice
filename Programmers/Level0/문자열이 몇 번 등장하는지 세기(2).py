
def solution(myString, pat):
    res = 0
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            res += 1
    return res

myString = "banana"
pat = "ana"
print(solution(myString, pat))
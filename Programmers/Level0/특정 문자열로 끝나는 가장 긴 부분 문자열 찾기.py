
def solution(myString, patStr):
    idx = myString.rfind(patStr)
    return myString[:idx + len(patStr)]

myString = "AAAAaaaa"
pat = "a"
print(solution(myString, pat))
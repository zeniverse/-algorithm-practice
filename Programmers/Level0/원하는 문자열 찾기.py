def solution(myString, pat):
    return 1 if pat.upper() in myString.upper() else 0

myString = "AbCdEfG"
pat = "aBc"
print(solution(myString, pat))
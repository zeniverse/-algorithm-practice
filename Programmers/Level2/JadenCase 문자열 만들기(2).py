
def solution(s):
    s = s.lower()
    s = list(s.split(" "))

    for i in range(len(s)):
        if s[i] and s[i][0].isalpha():
                s[i] = s[i][0].upper() + s[i][1:]

    return " ".join(s)

s ="3people  unFollowed me"
print(solution(s))



s = "3people unFollowed me"

res = s[0].upper()

for i in range(1, len(s)):
    if s[i - 1] == ' ' and s[i] != ' ':
        res += s[i].upper()
    else:
        res += s[i].lower()

print(res)



# 65-90
# 97~122

s = "AaZz"
n = 25

s = list(s)

for i in range(len(s)):
    if s[i].isupper():
        s[i] = chr((ord(s[i]) - ord('A') + n)%26 + ord('A'))
    elif s[i].islower():
        s[i] = chr((ord(s[i]) - ord('a') + n)%26 + ord('a'))

print("".join(s))


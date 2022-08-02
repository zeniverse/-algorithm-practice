s = "try hello world"
s = s.upper()
s = list(s)
tmp = ''
count = 0

for i in range(len(s)):
    if s[i] == ' ':
        tmp = ''
        count = 0
    else:
        if count % 2 != 0:
            s[i] = s[i].lower()
            
        count += 1

print("".join(s))
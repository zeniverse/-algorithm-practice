
s = 'baabaa'

stack = []
stack.append(s[0])

for i in range(1, len(s)):
    if stack:
        if stack[-1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    else:
        stack.append(s[i])

if stack:
    print(0)
else:
    print(1)







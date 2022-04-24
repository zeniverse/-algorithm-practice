s = input()
res = []

for i in range(len(s)):
    res.append(s[i:])

[print(i) for i in sorted(res)]